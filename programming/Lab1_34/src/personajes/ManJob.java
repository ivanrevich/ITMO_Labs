package personajes;

import java.util.Random;

public enum ManJob {
    FARMER,
    GUARDER;

    private static final Random RANDOM = new Random();
    private static final ManJob[] manJobs = values();

    public static ManJob random() {
        return manJobs[RANDOM.nextInt(manJobs.length)];
    }
}
