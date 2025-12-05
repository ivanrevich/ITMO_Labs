package things.weapons;

import org.jetbrains.annotations.NotNull;

public record Helmet() {
    @NotNull
    @Override
    public String toString() {
        return "шлем";
    }
}
