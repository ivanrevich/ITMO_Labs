package nature;

public class Sky extends NatureObject{
    public Sky() {
        super("небо");
    }

    @Override
    public String toString() {
        return super.title;
    }

    @Override
    public void appeared() {
        System.out.println(title+" появилось из-за туч");
    }

    @Override
    public void misapprehended() {

        System.out.println(title+" скрылось из-за туч");
    }
}
