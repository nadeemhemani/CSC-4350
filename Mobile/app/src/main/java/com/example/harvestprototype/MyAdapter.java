package com.example.harvestprototype;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {

    LayoutInflater inflater;
    List<Store> stores;
    List<Food> foods;
    public MyAdapter(Context context, List<Store> stores, List<Food> foods) {
        this.inflater = LayoutInflater.from(context);
        this.stores = stores;
        this.foods = foods;
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
        //test code

        Food food = foods.get(position);
        holder.foodText.setText(foods.get(position).getName());
        boolean isExpanded = foods.get(position).isExpanded();
        holder.expandableLayout.setVisibility(isExpanded ? View.VISIBLE : View.GONE);
    }



    @Override
    public int getItemCount()
    {
        return stores.size();
    }


    // have to change this
    public class MyViewHolder extends RecyclerView.ViewHolder {
        ConstraintLayout expandableLayout, MainCardLayout;
        TextView nameText, distanceText, addressText, phoneText, hoursText, itemsText, foodText;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            nameText = itemView.findViewById(R.id.nameView);
            distanceText = itemView.findViewById(R.id.distanceView);
            addressText = itemView.findViewById(R.id.addressView);
            phoneText = itemView.findViewById(R.id.phoneView);
            hoursText = itemView.findViewById(R.id.hoursView);
            itemsText = itemView.findViewById(R.id.itemsView);

            foodText = itemView.findViewById(R.id.foodView);
            expandableLayout = itemView.findViewById(R.id.expandableLayout);
            MainCardLayout = itemView.findViewById(R.id.MainCard);


            MainCardLayout.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    Food food = foods.get(getAdapterPosition());
                    food.setExpanded(!food.isExpanded());
                    notifyItemChanged(getAdapterPosition());

                }
            });
        }
    }
}