package personajes;

import things.Thing;
import things.weapons.Helmet;
import things.weapons.Spear;

public class Personage extends Man{
    private ManJob manJob;
    private Thing[] ownThings;/// don't work

    public Personage(String name, ManJob manJob) {
        super(name, ManMood.randomMood());
        this.manJob = manJob;
        if(manJob==ManJob.GUARDER){
            ownThings = new Thing[]{new Helmet(), new Spear()}
        }
    }

    public void contact(Man man){
        System.out.println();
    }

    public ManJob getManJob() {
        return manJob;
    }

    public void setManJob(ManJob manJob) {
        this.manJob = manJob;
    }

    @Override
    public void go() {
        System.out.println(super.getName()+" ходил");
    }

    @Override
    public void see(Thing thing) {
        System.out.println(super.getName()+" увидел");
    }

    @Override
    public String toString() {
        return super.toString();
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
