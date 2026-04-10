from ex0 import AquaFactory, FlameFactory, CreatureFactory, Creature


def check_factory(factory: CreatureFactory) -> bool:
    if (factory is None):
        return False
    base: Creature = factory.create_base("Base")
    if (base is None):
        return False
    print(base.describe())
    print(base.attack())
    evolved: Creature = factory.create_evolved("Evolved")
    if (evolved is None):
        return False
    print(evolved.describe())
    print(evolved.attack())


def make_em_fight(aquaFactory: AquaFactory, flameFactory: FlameFactory):
    criature_aqua: Creature = aquaFactory.create_base("Aquabub")
    criature_flame: Creature = flameFactory.create_base("Flameling")
    print(criature_aqua.describe())
    print(criature_flame.describe())

    print(criature_aqua.attack())
    print(criature_flame.attack())


def main():
    factory_aqua = AquaFactory()
    factory_flame = FlameFactory()
    print("Testing factory")
    check_factory(factory_aqua)
    print()
    print("Testing factory")

    check_factory(factory_flame)
    print()

    print("Testing battle")
    make_em_fight(factory_aqua, factory_flame)


if __name__ == "__main__":
    main()
