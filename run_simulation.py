from mtg_optimizer.builders.deck_builders import build_zur
from mtg_optimizer.structs.game import Game
from mtg_optimizer.structs.statistics import Statistics
from mtg_optimizer.strategies.strategy import StrategyZur
from tqdm import tqdm

if __name__ == '__main__':
    num_sims = 10000
    strat = StrategyZur()
    stats = Statistics()

    for i in tqdm(range(num_sims)):
        zur_deck = build_zur(counts=[27, 11, 7, 8, 3, 6, 5, 9, 4, 12, 7, 0])
        #zur_deck = build_zur(counts=[36, 11, 1, 21, 2, 2, 1, 2, 9, 10, 3, 1])
        game = Game(deck=zur_deck, strat=strat, stats=stats, turn_limit=10)
        game.run()

    print(stats)

    metric = stats.finalize()
    print(f"Simulation performance: {round(metric, 2)}")

# TODO:
# meter o codigo do main numa func permite usar essa func como objetivo de otimizacao para algoritmos de optim