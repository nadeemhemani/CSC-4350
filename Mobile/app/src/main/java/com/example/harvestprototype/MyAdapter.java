package com.example.harvestprototype;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {

    LayoutInflater inflater;
    List<Store> stores;

    public MyAdapter(Context context, List<Store> stores) {
        this.inflater = LayoutInflater.from(context);
        this.stores = stores;
    }


    // might need to be changed
    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = inflater.inflate(R.layout.store_row, parent,false);
        return new MyViewHolder(view);
    }


    // have to change this
    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {

        holder.nameText.setText(stores.get(position).getName());
        holder.distanceText.setText(stores.get(position).getDistance());
        holder.addressText.setText(stores.get(position).getAddress());
        holder.phoneText.setText(stores.get(position).getPhone());
        holder.hoursText.setText(stores.get(position).getHours());
        holder.itemsText.setText(stores.get(position).getItems());
    }


    @Override
    public int getItemCount() {
        return stores.size();
    }


    // have to change this
    public class MyViewHolder extends RecyclerView.ViewHolder {

        TextView nameText, distanceText, addressText, phoneText, hoursText, itemsText;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            nameText = itemView.findViewById(R.id.nameView);
            distanceText = itemView.findViewById(R.id.distanceView);
            addressText = itemView.findViewById(R.id.addressView);
            phoneText = itemView.findViewById(R.id.phoneView);
            hoursText = itemView.findViewById(R.id.hoursView);
            itemsText = itemView.findViewById(R.id.itemsView);
        }
    }

}
