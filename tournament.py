import itertools

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def run_tournament(
    title: str, opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(f"Tournament {title}")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for (fac1, strat1), (fac2, strat2) in itertools.combinations(opponents, 2):
        print("\n* Battle *")
        c1 = fac1.create_base()
        c2 = fac2.create_base()

        print(c1.describe())
        print("VS.")
        print(c2.describe())
        print("now fight!")

        try:
            strat1.act(c1)
            strat2.act(c2)
        except InvalidStrategyError as e:
            print(f"Battle error, aborting tournament: {e}")
            return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggro = AggressiveStrategy()
    defense = DefensiveStrategy()

    run_tournament("(basic)", [(flame, normal), (heal, defense)])
    print()
    run_tournament("(error)", [(flame, aggro), (heal, defense)])
    print()
    run_tournament(
        "(multiple)", [(aqua, normal), (heal, defense), (transform, aggro)]
    )


if __name__ == "__main__":
    main()
