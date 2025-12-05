package personajes;

import things.Thing;
import things.weapons.Helmet;
import things.weapons.Spear;

import java.util.Random;

public class Personage extends Man{
    private ManJob manJob;
    private Helmet helmet;
    private Spear spear;

    public Personage(String name, ManJob manJob, ManMood mood) {
        super(name, mood);
        this.manJob = manJob;
        if(manJob==ManJob.GUARDER){
            helmet = new Helmet();
            spear = new Spear();
        }
    }

    public Personage() {
        Random random = new Random();
        String[] names = {"Ганс", "Чербурашка", "Мальвина", "Незнайка", "Аркадий", "Ибрагим", "Василий"};
        super(names[random.nextInt(0, names.length)], ManMood.randomMood());
        this.manJob=ManJob.random();
    }

    public void contact(Man man){
        /// HINGE SOUND AND DOORS
        System.out.println(man.getName()+" увидел "+getMood()+" "+manJob.toString()+" которого звали "+this.getName());
        if(helmet!=null){
            System.out.println("У него был "+ helmet);
        }
        if(spear!=null){
            System.out.println("У него было "+ spear);
        }
        super.randomUpdateMood();
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
