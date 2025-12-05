package things.buildings;

import java.util.Random;

public class Door extends Building{
    Hinge[] hinges = new Hinge[4];
    private boolean isOpen = false;
    protected Door(String title, Material material) {
        super(title, material);
        for(int i=0; i<hinges.length; i++){
            hinges[i] = new Hinge();
        }
    }

    public boolean isOpen() {
        return isOpen;
    }

    public String getDoorState() {
        if (isOpen){
            return "Окрыта";
        }
        return "закрыта";
    }

    public void tryToOpen(){
        Random random = new Random();
        if(random.nextInt(0, 3)==2){
            setOpen(true);
            for(Hinge h:hinges){
                h.playSound();
            }
            System.out.println(title+" открылась, как будто приглашая войти");
        }else{
            System.out.println(title+" не открылась");
        }
    }

    private void setOpen(boolean open) {
        isOpen = open;
    }

    @Override
    public String toString() {
        return super.toString()+" "+getDoorState();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }
}
