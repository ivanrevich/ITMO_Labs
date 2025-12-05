package things.buildings;

import things.Sound;
import things.Thing;

public class Hinge extends Thing {
    private Sound sound;

    public Hinge() {
        super("петля");
        sound = Sound.random();
    }

    public void playSound(){
        System.out.println(title+" издала "+sound.toString());
    }

    public Sound getSound() {
        return sound;
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
