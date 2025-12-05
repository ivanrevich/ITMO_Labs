package things;

public abstract class Thing {
    public final String title;
    private ThingState state;

    protected Thing(String title) {
        this.title = title;
        state = ThingState.EXIST;
    }

    public void changeVisibleState(){
        if(state==ThingState.APPEARED ){
            misapprehended();
        }else if(state==ThingState.MISAPPREHENDED || state == ThingState.EXIST){
            appeared();
        }
    }

    public void appeared(){
        state = ThingState.APPEARED;
        System.out.println(title+" появилось");
    }
    public void misapprehended(){
        state = ThingState.MISAPPREHENDED;
        System.out.println(title+" исчезло");
    }


}
