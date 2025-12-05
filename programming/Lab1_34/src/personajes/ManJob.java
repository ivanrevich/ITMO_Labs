package personajes;

import java.util.Random;

public enum ManJob {
    FARMER("фермер"),
    KING("король"),
    GUARDER("охранник");

    private final String title;
    ManJob(String s) {
        title=s;
    }


    private static final Random RANDOM = new Random();
    private static final ManJob[] manJobs = values();

    public static ManJob random() {
        return manJobs[RANDOM.nextInt(0, manJobs.length)];
    }

    @Override
    public String toString() {
        return title;
    }
}
