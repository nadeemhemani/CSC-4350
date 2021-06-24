package com.example.harvestprototype;

import java.util.ArrayList;
import java.util.List;

public class Store {

    private String name, distance, address, phone, hours, items, latitude, longitude, id;
    private List<Food> foods = new ArrayList<>();
    private List<String> foodNames = new ArrayList<>();

    public Store() {

    }
    // need to add list to constructor
    public Store(String name, String distance, String address, String phone, String hours, String items, String latitude, String longitude, String id) {
        this.name = name;
        this.distance = distance;
        this.address = address;
        this.phone = phone;
        this.hours = hours;
        this.items = items;
        this.latitude = latitude;
        this.longitude = longitude;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getHours() {
        return hours;
    }

    public void setHours(String hours) {
        this.hours = hours;
    }

    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }

    public Double getLatitude() {
        return Double.parseDouble(latitude);
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    public Double getLongitude() {
        return Double.parseDouble(longitude);
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }

    public void setFoods(List<Food> foods) {
        this.foods = foods;
    }

    public void addFood(Food food) {
        foods.add(food);
    }

    public List<Food> getFoods() {
        return foods;
    }

    public List<String> getFoodNames() {
        for (Food food : foods) {
            foodNames.add(food.getName());
        }
        return  foodNames;
    }

    public String getId(){return id;}

}
