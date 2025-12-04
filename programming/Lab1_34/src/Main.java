import nature.NatureObject;
import nature.Sea;
import nature.Sky;
import personajes.MainHero;
import personajes.Personage;
import things.Thing;
import things.buildings.Castle;
import things.buildings.Door;
import things.buildings.Tower;
import things.buildings.Wall;

public class Main {
    public void main(String[] args){
        World world;
        Castle castle;

        Door[] doors = new Door[(int) (Math.random() * 3)];
        Tower[] towers = new Tower[(int) (Math.random() * 8)];
        Wall[] walls  = new Wall[4+(int) (Math.random() * 6)];

        castle = new Castle("Замок", doors, towers, walls);

        Sea sea = new Sea();
        Sky sky = new Sky();

        //// GENERATING MAIN HERO
        MainHero mainHero = new MainHero("Нильс");

        //// GENERATING PERSONAGES
        int countOfPersonages =  (int) (Math.random() * 20);
        Personage[] personages = new Personage[countOfPersonages];
        for(int i = 0; i<countOfPersonages; i++){
            personages[i] = new Personage("Name "+String.valueOf(i));
        }


        world = new World(personages, mainHero, new Thing[]{castle,sea, sky});
        world.Interact();
    }
}
