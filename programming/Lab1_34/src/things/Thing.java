package things;

public abstract class Thing {
    public final String title;
    ThingState state;

    protected Thing(String title) {
        this.title = title;
        state = ThingState.EXIST;
    }

    void appeared(){
        state = ThingState.APPEARED;
        System.out.println(title+" появилось");
    }
    void misapprehended(){
        state = ThingState.MISAPPREHENDED;
        System.out.println(title+" исчезло");
    }


}
