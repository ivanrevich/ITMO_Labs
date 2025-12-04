package things.buildings;

import things.Thing;

public class Castle extends Building{
    private Door[] doors;
    private Tower[] towers;
    private Wall[] walls;


    public Door[] getDoors() {
        return doors;
    }

    public void setDoors(Door[] doors) {
        this.doors = doors;
    }

    public Tower[] getTowers() {
        return towers;
    }

    public void setTowers(Tower[] towers) {
        this.towers = towers;
    }

    public Wall[] getWalls() {
        return walls;
    }

    public void setWalls(Wall[] walls) {
        this.walls = walls;
    }

    public Castle(String title, Door[] doors, Tower[] towers, Wall[] walls) {
        super(title);
        this.doors = doors;
        this.towers = towers;
        this.walls = walls;
    }

    @Override
    public String toString() {
        return super.title;
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
