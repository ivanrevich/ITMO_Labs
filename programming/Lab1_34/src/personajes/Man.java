package personajes;

public abstract class Man implements BaseMove{
    String name;
    ManMood mood;

    public Man(String name, ManMood mood) {
        this.name = name;
        this.mood = mood;
    }
}
