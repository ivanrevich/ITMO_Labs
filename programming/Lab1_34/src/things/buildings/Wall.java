package things.buildings;

public class Wall extends Building{
    protected Wall() {
        super("стена");
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
