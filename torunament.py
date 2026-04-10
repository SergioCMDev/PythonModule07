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



    factory_aqua = AquaFactory()
    factory_flame = FlameFactory()
    flameling: Creature = factory_flame.create_base()
    sproutling: Creature = healingCreatureFactory.create_base()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")


    print("* Battle *")
    flameling.describe()
    print("vs")
    sproutling.describe()
    print("now fight")


def battle(opponents: list[tuple[Creature, BattleStrategy]]) -> None:
    if (len(opponents) < 0):
        print("Error en la batalla")
        return
    pass


if __name__ == "__main__":
    main()
