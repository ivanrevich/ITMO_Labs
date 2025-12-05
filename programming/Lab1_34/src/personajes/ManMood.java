package personajes;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public enum ManMood {
    DREAM,
    WORK,
    ANGRY,
    FIGHT,
    DIE,
    BORN,
    HUNGRY;
    private static final Random RANDOM = new Random();
    private static final ManMood[] MOODS = values();

    public static ManMood randomMood() {
        return MOODS[RANDOM.nextInt(MOODS.length)];
    }
}
