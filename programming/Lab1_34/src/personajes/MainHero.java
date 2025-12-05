package personajes;

import things.Thing;

import java.util.ArrayList;
import java.util.Random;

public class MainHero extends Man implements ExtendedMove{
    public ArrayList<Thing> seenThings = new ArrayList<Thing>();

    public ArrayList<Personage> seenPersons = new ArrayList<Personage>();

    private Random random = new Random();
    public MainHero(String name){
        super(name, ManMood.BORN);
    }
    @Override
    public void headUp() {
        System.out.println(super.getName()+" поднял голову");
    }

    @Override
    public void think(String thought) {
        System.out.println("'"+thought+"' - подумал " + super.getName());
    }

    @Override
    public void fastOpenCloseEyes() {
        System.out.println(super.getName()+" крепко-накрепко зажмурил глаза и быстро открыл их");
    }

    @Override
    public void goTo(Thing thing) {
        int variant = random.nextInt(4);
        if (variant == 1) {
            System.out.println(super.getName() + " подошёл поближе к "+thing.toString());
        } else if (variant == 2) {
            System.out.println(super.getName() + " подбежал к "+thing.toString());
        } else if (variant == 3) {
            System.out.println(super.getName() + " пришёл к "+thing.toString());
        }
    }

    @Override
    public Boolean checkMood(ManMood mood) {
        return getMood()==mood;
    }

    @Override
    public void go() {
        int variant = random.nextInt(4);
        if (variant == 1) {
            System.out.println(super.getName() + " зашагал дальше");
        } else if (variant == 2) {
            System.out.println(super.getName() + " пошел ");
        } else if (variant == 3) {
            System.out.println(super.getName() + " побежал");
        }
    }

    @Override
    public void see(Thing thing) {
        seenThings.add(thing);
        int variant = random.nextInt(4);
        if(variant==1) {
            System.out.println(super.getName() + " посмотрел на " + thing.toString());
        } else if (variant==2) {
            System.out.println("Прямо перед "+super.getName() + " была " + thing.toString());
        } else if (variant==3) {
            System.out.println(super.getName() + " стал рассматривать " + thing.toString());
        }
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
