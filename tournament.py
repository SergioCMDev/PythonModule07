from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex0 import AquaFactory, CreatureFactory, FlameFactory, Creature
from ex2 import (
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    AggressiveStrategy,
)


def main() -> None:
    healingCreatureFactory = HealingCreatureFactory()
    transformCreatureFactory = TransformCreatureFactory()

    defensiveStrategy = DefensiveStrategy()
    normalStrategy = NormalStrategy()
    aggressiveStrategy = AggressiveStrategy()
    healingCreatureFactory.create_base()

    factory_aqua = AquaFactory()
    factory_flame = FlameFactory()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(
        [(factory_flame, normalStrategy),
         (healingCreatureFactory, defensiveStrategy)],
    )
    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(
        [(factory_flame, aggressiveStrategy),
         (healingCreatureFactory, defensiveStrategy)],
    )
    print()
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [(factory_aqua, normalStrategy),
         (healingCreatureFactory, defensiveStrategy),
         (transformCreatureFactory, aggressiveStrategy)

         ],
    )


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    if (len(opponents) < 2):
        raise Exception("Error en la entrada")

    for factory, strategy in opponents:
        if (factory is None or strategy is None):
            raise Exception("Error en la entrada")
        if not callable(getattr(factory, "create_base", None)):
            raise TypeError("factory sin create_base")
        if not callable(getattr(factory, "create_evolved", None)):
            raise TypeError("factory sin create_evolved")
        if not callable(getattr(strategy, "act", None)):
            raise TypeError("strategy sin act")
        if not callable(getattr(strategy, "is_valid", None)):
            raise TypeError("strategy sin is_valid")

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(0, len(opponents)):

        criature_a: Creature = opponents[i][0].create_base("Criature A")
        strategy_a = opponents[i][1]

        for j in range(i+1, len(opponents)):
            criature_b: Creature = opponents[j][0].create_base("Criature B")
            strategy_b = opponents[j][1]
            print()
            print("* Battle *")
            print(criature_a.describe())
            print(" vs")
            print(criature_b.describe())
            print(" now fight")
            if (not strategy_b.is_valid(criature_b)):
                print("Battle error, aborting tournament: "
                      f"strategy '{type(strategy_b).__name__}' is not valid "
                      f"for creature '{type(criature_b).__name__}'")
                continue
            if (not strategy_a.is_valid(criature_a)):
                print("Battle error, aborting tournament: "
                      f"strategy '{type(strategy_a).__name__}' is not valid "
                      f"for creature '{type(criature_a).__name__}'")
                continue
            strategy_a.act(criature_a)
            strategy_b.act(criature_b)


if __name__ == "__main__":
    main()
