package com.example.harvestprototype;

public class Food {
    private String name, qty, cals, exp;
    private boolean expanded;

    public Food() {

    }

    public Food(String name){
        this.name = name;
        this.expanded = false;

    }

    public void setName(String name) {
        this.name = name;
    }

    public void setQty(String name) {
        this.qty = qty;
    }

    public void setCals(String name) {
        this.cals = cals;
    }

    public void setExp(String name) {
        this.exp = exp;
    }


    public String getName() {
        return name;
    }


    @Override
    public String toString() {
        return "Food{" +
                "name='" + name+ '}';
    }

    public boolean isExpanded() {
        return expanded;
    }

    public void setExpanded(boolean expanded) {
        this.expanded = expanded;
    }
}
