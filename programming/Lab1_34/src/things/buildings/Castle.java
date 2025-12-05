package things.buildings;

import things.Thing;

import java.util.ArrayList;
import java.util.Random;

public class Castle extends Building{
    private Door[] doors;
    private Tower[] towers;
    private Wall[] walls;

    public Castle() {
        super("замок", Material.random());
        Random random = new Random();

        doors = new Door[random.nextInt(1, 5)];
        for(int i=0; i<doors.length; i++){
            doors[i] = new Door("Дверь "+i, Material.random());
        }

        towers = new Tower[random.nextInt(1, 5)];
        for(int i=0; i<towers.length; i++){
            towers[i] = new Tower("Башня "+i, Material.random());
        }

        walls = new Wall[random.nextInt(1, 5)];
        for(int i=0; i<walls.length; i++){
            walls[i] = new Wall("стена "+i, Material.random());
        }

    }


    public Thing[] getAllConstructions(){
        ArrayList<Thing> alls= new ArrayList<Thing>();

        for(Wall w: walls){
            alls.add(w);
        }
        for(Tower t: towers){
            alls.add(t);
        }
        for(Door d: doors){
            alls.add(d);
        }
        return alls.toArray(Thing[]::new);
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
