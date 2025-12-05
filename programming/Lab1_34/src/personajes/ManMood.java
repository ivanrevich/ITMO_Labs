package personajes;

import java.util.Random;

public enum ManMood {
    DREAM("спит"),
    WORK("работает"),
    ANGRY("злой"),
    FIGHT("напал"),
    HUNGRY("голодный");

    private final String title;
    ManMood(String s) {
        title=s;
    }

    private static final Random RANDOM = new Random();
    private static final ManMood[] MOODS = values();

    public static ManMood randomMood() {
        return MOODS[RANDOM.nextInt(MOODS.length)];
    }

    @Override
    public String toString() {
        return title;
    }
}
