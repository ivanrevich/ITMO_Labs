package pokemons;

import attacks.physical.BoneRush;
import attacks.physical.Facade;
import attacks.physical.FuryAttack;
import attacks.special.ShadowBall;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Mandibuzz extends Pokemon {
    public Mandibuzz(String name, int level){
        super(name, level);
        setStats(110, 65, 105, 55, 95, 80);
        setType(Type.DARK, Type.FLYING);
        setMove(new Facade(), new FuryAttack(), new ShadowBall(), new BoneRush());
    }
}
