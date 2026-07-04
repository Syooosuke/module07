from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def format_opponent(fac: CreatureFactory, strat: BattleStrategy) -> str:
    fac_name = fac.__class__.__name__.replace("CreatureFactory", "").replace(
        "Factory", ""
    )
    if fac_name == "Flame":
        fac_name = "Flaming"
    elif fac_name == "Aqua":
        fac_name = "Aquabub"

    strat_name = strat.__class__.__name__.replace("Strategy", "")

    return f"({fac_name}+{strat_name})"


def run_tournament(
    title: str, opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(f"Tournament {title}")
    opp_strs = [format_opponent(fac, strat) for fac, strat in opponents]
    print(f"[ {', '.join(opp_strs)}]")

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    num_opponents = len(opponents)
    for i in range(num_opponents - 1):
        for j in range(i + 1, num_opponents):
            fac1, strat1 = opponents[i]
            fac2, strat2 = opponents[j]

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

    run_tournament("0 (basic)", [(flame, normal), (heal, defense)])
    print()
    run_tournament("1 (error)", [(flame, aggro), (heal, defense)])
    print()
    run_tournament(
        "2 (multiple)", [(aqua, normal), (heal, defense), (transform, aggro)]
    )


if __name__ == "__main__":
    main()
