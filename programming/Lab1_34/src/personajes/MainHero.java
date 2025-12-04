package personajes;

import things.Thing;

import java.util.ArrayList;

public class MainHero extends Man implements ExtendedMove{
    public ArrayList<Thing> seenThings = new ArrayList<Thing>();

    public MainHero(String name){
        super(name, ManMood.BORN);
    }
    @Override
    public void headUp() {

    }

    @Override
    public void think() {

    }

    @Override
    public void go() {

    }

    @Override
    public void see(Thing thing) {
        seenThings.add(thing);
        //TODO: чередование рандомное увидел/посмотрел на
        System.out.println(super.name+" увидел "+thing.toString());
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
