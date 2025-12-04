package personajes;

import things.Thing;

public class Personage extends Man{


    public Personage(String name) {
        super(name, ManMood.randomMood());
    }

    @Override
    public void go() {

    }

    @Override
    public void see(Thing thing) {

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
