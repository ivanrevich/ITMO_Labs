package things.weapons;

import org.jetbrains.annotations.NotNull;

public record Spear() {
    @NotNull
    @Override
    public String toString() {
        return "копьё";
    }
}
