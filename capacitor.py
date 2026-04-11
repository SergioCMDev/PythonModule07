from ex1 import TransformCreatureFactory, HealingCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")

    healingCreatureFactory = HealingCreatureFactory()
    transformCreatureFactory = TransformCreatureFactory()

    heal_base_creature = healingCreatureFactory.create_base("Sproutling")
    heal_evolved_creature = healingCreatureFactory.create_evolved("Bloomelle")

    transform_base_creature = transformCreatureFactory.create_base("Shiftling")
    transform_evolved_creature =  \
        transformCreatureFactory.create_evolved("Morphagon")

    print(heal_base_creature.describe())
    print(heal_base_creature.attack())
    print(heal_base_creature.heal())
    print(" evolved:")
    print(heal_evolved_creature.describe())
    print(heal_evolved_creature.attack())
    print(heal_evolved_creature.heal())
    print()
    print("Testing Creature with transform capability")
    print(" base:")
    print(transform_base_creature.describe())
    print(transform_base_creature.attack())
    print(transform_base_creature.transform())
    print(transform_base_creature.attack())
    print(transform_base_creature.revert())
    print(" evolved:")
    print(transform_evolved_creature.describe())
    print(transform_evolved_creature.attack())
    print(transform_evolved_creature.transform())
    print(transform_evolved_creature.attack())
    print(transform_evolved_creature.revert())


if __name__ == "__main__":
    main()
