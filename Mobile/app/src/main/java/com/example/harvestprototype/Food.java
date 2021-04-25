package com.example.harvestprototype;

public class Food {
    private String name;
    private boolean expanded;
    public Food(String name){
        this.name = name;
        this.expanded = false;

    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
