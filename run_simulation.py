from mtg_optimizer.builders.deck_builders import build_zur
from mtg_optimizer.structs.game import Game
from mtg_optimizer.structs.statistics import Statistics
from mtg_optimizer.strategies.strategy import Strategy
from tqdm import tqdm

if __name__ == '__main__':
    num_sims = 10 #10000
    strat = Strategy()
    stats = Statistics()

    for i in tqdm(range(num_sims)):
        zur_deck = build_zur()
        game = Game(deck=zur_deck, strat=strat, stats=stats, turn_limit=10)
        game.run()

    print(stats)

    metric = stats.finalize()
    print(f"Simulation performance: {round(metric, 2)}")

# TODO:
# meter o codigo do main numa func permite usar essa func como objetivo de otimizacao para algoritmos de optim