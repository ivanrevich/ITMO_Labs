package things.buildings;

public class Wall extends Building{
    protected Wall(String name, Material material) {
        super(name, Material.random());
    }

    @Override
    public String toString() {
        return super.title;
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }
}
