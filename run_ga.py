import pygad

from mtg_optimizer.builders.deck_builders import build_zur
from mtg_optimizer.structs.game import Game
from mtg_optimizer.structs.statistics import Statistics
from mtg_optimizer.strategies.strategy import StrategyZur

from collections import Counter
import time
import logging


def translate_genotype(genotype, card_types=12):
    counts = Counter(genotype)
    fenotype = [counts[c] for c in range(card_types)]
    return fenotype


def fitness_func(ga_instance, solution, solution_idx):
    num_sims = 10
    strat = StrategyZur()
    stats = Statistics()

    for i in range(num_sims):
        fenotype=translate_genotype(solution)
        zur_deck = build_zur(counts=fenotype)
        game = Game(deck=zur_deck, strat=strat, stats=stats, turn_limit=10)
        game.run()

    fitness = stats.finalize()
    return fitness


if __name__ == '__main__':
    t0 = time.time()
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    """

    config_dict = {
        'gene_type': int,
        'parallel_processing': ('process', 10), #TODO: optimise this
        #'logger': logger,
        'num_generations': 15,
        'num_parents_mating': 2,
        'fitness_func': fitness_func,
        'sol_per_pop': 20,
        'num_genes': 99,
        'init_range_low': 0,
        'init_range_high': 12,
        'parent_selection_type': "tournament",
        'K_tournament': 4,
        'crossover_type': "single_point",
        #'crossover_probability': 0.5,
        'mutation_type': "random",
        'mutation_percent_genes': 5,
        'keep_elitism': 0,
        'keep_parents': 0,
        'save_solutions': False,
        'save_best_solutions': False,
    }

    ga_instance = pygad.GA(**config_dict)

    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    solution = translate_genotype(solution)
    best_deck = build_zur(counts=solution)

    print(solution)
    print(f"FITNESS: {solution_fitness}")
    #print(ga_instance.summary())

    ga_instance.plot_fitness()
    #ga_instance.plot_genes(graph_type="boxplot", solutions='all')

    print("Time elapsed", time.time() - t0)
