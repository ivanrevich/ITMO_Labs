package things.buildings;

import things.Thing;

public abstract class Building extends Thing {
    protected Building(String title) {
        super(title);
    }


    @Override
    public String toString() {
        return super.toString();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }
}
