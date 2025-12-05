package things.buildings;

import personajes.ManMood;

import java.util.Random;

public enum Material{
    WOOD("дерева"),
    STONE("камня"),
    UNHANDLED_BIG_STONES("крупных необтесанных камней");

    private final String name;
    Material(String s) {
        this.name = s;
    }

    private static final Random RANDOM = new Random();
    private static final Material[] Materials = values();

    public static Material random() {
        return Materials[RANDOM.nextInt(Materials.length)];
    }


    @Override
    public String toString() {
        return name;
    }
}
