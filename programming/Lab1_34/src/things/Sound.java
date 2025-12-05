package things;

import java.util.Random;

public enum Sound {
    CREAK("скрежет"),
    SCRATCH("скрип"),
    NO_SOUND("беззвучно");


    private final String title;

    Sound(String title) {
        this.title = title;
    }

    @Override
    public String toString() {
        return title;
    }

    private static final Random RANDOM = new Random();
    private static final Sound[] sounds = values();

    public static Sound random() {
        return sounds[RANDOM.nextInt(0, sounds.length)];
    }

}
