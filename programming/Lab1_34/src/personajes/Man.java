package personajes;

public abstract class Man implements BaseMove{
    private String name;
    private ManMood mood;

    public Man(String name, ManMood mood) {
        this.name = name;
        this.mood = mood;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ManMood getMood() {
        return mood;
    }

    public void setMood(ManMood mood) {
        this.mood = mood;
    }
}
