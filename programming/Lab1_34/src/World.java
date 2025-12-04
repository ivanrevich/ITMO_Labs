import personajes.MainHero;
import personajes.Personage;
import things.Thing;
import things.buildings.*;

import java.util.Random;

public class World {
    public MainHero hero;
    public Personage[] personages;
    public Thing[] things;

    public World(Personage[] personages, MainHero hero, Thing[] things) {
        this.personages = personages;
        this.hero = hero;
        this.things = things;
    }


    public void Interact(){
        Random random = new Random();
        while(hero.seenThings.size()!=things.length) {
            int randIdx = random.nextInt(things.length);
            Thing th = things[randIdx];
            if (!hero.seenThings.contains(th)) {
                hero.see(th);
            }
        }
    }
}
