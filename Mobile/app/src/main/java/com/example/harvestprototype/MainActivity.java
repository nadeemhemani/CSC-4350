package com.example.harvestprototype;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.fragment.app.FragmentActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.toolbox.JsonArrayRequest;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.JsonObject;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

import afu.org.checkerframework.checker.igj.qual.I;

/**************************************************************************************************
 Final Harvest Prototype For Sprint-2!


 1. have to create adapter in myadapoter
 2. have to loop through each store in initdata
 3. have to change xml


 -- food request isnt working for some reason
 *************************************************************************************************/

public class MainActivity extends FragmentActivity implements OnMapReadyCallback, LocationListener {

    // Location:
    LocationManager locationManager;
    Location location;

    // Volley:
    private RequestQueue queue;
    private RequestQueue queueFood;
    List<Store> stores = new ArrayList<>();

    // RecyclerView:
    RecyclerView recyclerView;

    //only for test
    List<Food> foodList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Location Permissions:
        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        if (ActivityCompat.checkSelfPermission(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(MainActivity.this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION}, 100);
        }
        // Get Location:
        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 100, MainActivity.this);
        location = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);

        // Get Data:
        queue = Volley.newRequestQueue(this);
        queueFood =  Volley.newRequestQueue(this);

        String urlBeginning = "https://team-um6.herokuapp.com/consumer/";
        String urlCoordinates = location.getLatitude() + "/" + location.getLongitude() + "/";
        String urlMetric = "miles"; // user preference
        String url = urlBeginning + urlCoordinates + urlMetric;

        String arrayName = "stores";

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                try {
                    JSONArray jsonArray = response.getJSONArray(arrayName);

                    for (int i = 0; i < jsonArray.length(); i++) {
                        Store store = new Store();

                        JSONObject object =jsonArray.getJSONObject(i);

                        store.setName(object.getString("name"));
                        store.setAddress(object.getString("street") + ", " + object.getString("city") + ", " + object.getString("state") + " " + object.getString("zipcode"));
                        store.setPhone(object.getString("phone"));
                        String hours = formatHours(object.getString("open at"), object.getString("close at"));
                        store.setHours(hours);
                        store.setItems("Items Available: " + object.getString("items available"));
                        Double distanceTemp = Double.parseDouble(object.getString("distance"));
                        @SuppressLint("DefaultLocale") String distance = String.format("%.1f", distanceTemp);
                        store.setDistance(distance + " " + urlMetric);
                        store.setLatitude(object.getString("latitude"));
                        store.setLongitude(object.getString("longitude"));


                        // food request
                        String storeid = object.getString("id");
                        String foodUrl = "https://team-um6.herokuapp.com/foods/" + storeid;
                        String arrayNameFood = "foods";

                        JsonObjectRequest requestFood = new JsonObjectRequest(Request.Method.GET, foodUrl, null, new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                try {
                                    JSONArray jsonArrayFood = response.getJSONArray(arrayNameFood);
                                    for (int j = 0; j < jsonArrayFood.length(); j++) {
                                        Food food = new Food();
                                        JSONObject objectFood =jsonArrayFood.getJSONObject(j);

                                        food.setName(objectFood.getString("name"));
                                        food.setQty(objectFood.getString("quantity"));
                                        food.setCals(objectFood.getString("calories"));
                                        food.setExp(objectFood.getString("expiration"));


                                        store.addFood(food);

                                    }
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }

                            }
                        }, new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                error.printStackTrace();
                            }
                        });
                        queueFood.add(requestFood);

                        stores.add(store);
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                // RecyclerView:
                recyclerView = findViewById(R.id.RecyclerView);
                MyAdapter adapter = new MyAdapter(getApplicationContext(), stores, foodList);
                recyclerView.setAdapter(adapter);
                recyclerView.setLayoutManager(new LinearLayoutManager(getApplicationContext()));

                // Generate Map:
                SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
                mapFragment.getMapAsync(MainActivity.this);

                //test code


                /*********************************************************************************
                 STOP! Anything that happens "after" receiving data should be called
                 within the onResponse function. Anything after "queue.add(request)"
                 will not execute. (from what i've found)
                 *********************************************************************************/
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                error.printStackTrace();
            }
        });
        queue.add(request);


        initData();
    }


    @Override
    public void onMapReady(GoogleMap googleMap) {

        // Set Markers:
        for (Store store : stores) {
            LatLng storeLocation = new LatLng(store.getLatitude(), store.getLongitude());
            Log.d("tag", "message");
            googleMap.addMarker(new MarkerOptions().position(storeLocation).title(store.getName()));
        }

        // Set uer location:
        LatLng userLocation = new LatLng(location.getLatitude(),location.getLongitude());
        googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(userLocation,10.5f));

    }


    @Override
    public void onLocationChanged(@NonNull Location location) {

    }


    // Helper functions:
    public String formatHours (String open, String close) {
        String hours;
        String openString;
        String closeString;
        String openHour = open.substring(0,2);
        String closeHour = close.substring(0,2);
        // :00
        String openMin = open.substring(2,5);
        String closeMin = close.substring(2,5);
        int openInt = Integer.parseInt(openHour);
        int closeInt = Integer.parseInt(closeHour);
        // open
        if (openInt < 13) {
            openString = String.valueOf(openInt) + openMin + " am";
        } else {
            openString = String.valueOf(openInt - 12) + openMin + " pm";
        }
        // close
        if (closeInt < 13) {
            closeString = String.valueOf(closeInt) + closeMin + " am";
        } else {
            closeString = String.valueOf(closeInt - 12) + closeMin + " pm";
        }
        hours = openString + " - " + closeString;
        return hours;
    }


    // Tried to sort stores by distance but it didn't work
    // probably something wrong with these functions
    public List<Store> sortDistances (List<Store> storeList) {
        List<Store> newList = new ArrayList<>();
        for (Store store : storeList) {
            double dist = Double.parseDouble(store.getDistance());
            if (dist == getMinDist(storeList)) {
                newList.add(store);
                storeList.remove(store);
            }
        }
        return newList;
    }

    public Double getMinDist (List<Store> storeList) {
        double minDist = 100.0;
        for (Store store : storeList) {
            if (Double.parseDouble(store.getDistance()) < minDist) {
                minDist = Double.parseDouble(store.getDistance());
            }
        }
        return minDist;
    }
    //new code(test)
    private void initData() {
        foodList = new ArrayList<>();
        foodList.add(new Food("Bread"));
        foodList.add(new Food("Butter"));
        foodList.add(new Food("Blackberry Biscuit"));

    }



}