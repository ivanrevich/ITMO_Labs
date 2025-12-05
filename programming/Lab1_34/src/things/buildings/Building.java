package things.buildings;

import things.Thing;

public abstract class Building extends Thing {
    private Material material;
    protected Building(String title, Material material) {
        super(title);
        this.material = material;
    }


    @Override
    public String toString() {
        return title + " из "+material;
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
