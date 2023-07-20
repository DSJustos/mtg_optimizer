from mtg_optimizer.builders.deck_builders import build_zur
from mtg_optimizer.structs.game import Game
from mtg_optimizer.structs.statistics import Statistics
from mtg_optimizer.strategies.strategy import Strategy
from tqdm import tqdm

if __name__ == '__main__':
    num_sims = 10000
    strat = Strategy()
    stats = Statistics()

    for i in tqdm(range(num_sims)):
        zur_deck = build_zur()

        game = Game(deck=zur_deck, strat=strat, stats=stats)
        game.run()

    print(stats)
    stats.finalize()

    print("")

# TODO:
#