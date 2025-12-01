package things.buildings;

public class Castle extends Building{
    Door[] doors;
    Tower[] towers;
    Wall[] walls;

    public Castle(String title, Door[] doors, Tower[] towers, Wall[] walls) {
        super(title);
        this.doors = doors;
        this.towers = towers;
        this.walls = walls;
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
