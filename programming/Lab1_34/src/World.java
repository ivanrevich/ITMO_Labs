import nature.NatureObject;
import nature.Sea;
import nature.Sky;
import personajes.MainHero;
import personajes.ManJob;
import personajes.ManMood;
import personajes.Personage;
import things.Thing;
import things.buildings.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class World {
    private MainHero hero;
    private Personage[] personages;
    private Sky sky;
    private Sea sea;
    private Castle castle;

    private ArrayList<Thing> AllThings = new ArrayList<Thing>();


    public World() {
        WorldGenerating();
    }

    private void WorldGenerating(){
        castle = new Castle();
        sea = new Sea();
        sky = new Sky();


        //// GENERATING MAIN HERO
        hero = new MainHero("Нильс");

        //// GENERATING PERSONAGES
        int countOfPersonages =  (int) (Math.random() * 20);
        personages = new Personage[countOfPersonages];
        for(int i = 0; i<countOfPersonages; i++){
            personages[i] = new Personage("Name "+ i, ManJob.random());
        }
        //// ADD IT TO WORLD OBJECTS
        AllThings.add(castle);
        AllThings.add(sea);
        AllThings.add(sky);

        AllThings.addAll(Arrays.asList(castle.getAllConstructions()));
    }

    public void PlayStory() {
        Random random = new Random();
        while (hero.seenThings.size() != AllThings.size()) {
            Personage pers = personages[random.nextInt(personages.length)];
            Thing th = AllThings.get(random.nextInt(AllThings.size()));
            if (!hero.seenThings.contains(th)) {
                if (random.nextBoolean() && th instanceof NatureObject) th.changeVisibleState();
                hero.see(th);
                if (random.nextInt(0, 10) == 5) {
                    hero.think("Может, я все-таки сплю?");
                    hero.fastOpenCloseEyes();
                    if (hero.checkMood(ManMood.DREAM)) {
                        hero.think("Похоже на сон");
                    } else {
                        hero.think("Да, нет вроде не сплю");
                    }
                    hero.see(th);
                }
                if (!hero.seenPersons.contains(pers)) {
                    pers.contact(hero);
                }
            }
        }
    }
}
