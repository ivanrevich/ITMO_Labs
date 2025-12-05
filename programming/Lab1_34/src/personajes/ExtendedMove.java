package personajes;

import things.Thing;

public interface ExtendedMove extends BaseMove{
    void headUp();
    void think(String thought);
    void fastOpenCloseEyes();
    void goTo(Thing thing);

    Boolean checkMood(ManMood mood);
}
