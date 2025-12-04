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

    private static final List<ManMood> VALUES = List.of(values());
    private static final int SIZE = VALUES.size();
    private static final Random RANDOM = new Random();

    public static ManMood randomMood()  {
        return VALUES.get(RANDOM.nextInt(SIZE));
    }
}
