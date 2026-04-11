from ex0 import AquaFactory, FlameFactory, CreatureFactory, Creature


def check_factory(factory: CreatureFactory) -> bool:
    if (factory is None):
        return False
    if not callable(getattr(factory, "create_base", None)):
        return False
    if not callable(getattr(factory, "create_evolved", None)):
        return False

    base: Creature = factory.create_base("Base")
    print(base.describe())
    print(base.attack())

    evolved: Creature = factory.create_evolved("Evolved")
    if (base is None or
        not callable(getattr(base, "describe", None))
            or not callable(getattr(base, "attack", None))):
        return False
    if (evolved is None or
        not callable(getattr(evolved, "describe", None))
            or not callable(getattr(evolved, "attack", None))):
        return False
    print(evolved.describe())
    print(evolved.attack())
    return True


def make_em_fight(aquaFactory: AquaFactory, flameFactory: FlameFactory):
    criature_aqua: Creature = aquaFactory.create_base("Aquabub")
    criature_flame: Creature = flameFactory.create_base("Flameling")
    print(criature_aqua.describe())
    print(" vs")
    print(criature_flame.describe())
    print(" fight")

    print(criature_aqua.attack())
    print(criature_flame.attack())


def main():
    factory_aqua = AquaFactory()
    factory_flame = FlameFactory()
    print("Testing factory")
    if (not check_factory(factory_flame)):
        print(f"{factory_flame} is not correct")
        return
    print()
    print("Testing factory")
    if (not check_factory(factory_aqua)):
        print(f"{factory_aqua} is not correct")
        return
    print()

    print("Testing battle")
    make_em_fight(factory_aqua, factory_flame)


if __name__ == "__main__":
    main()
