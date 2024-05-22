import typing
from typing_extensions import List, Tuple
import random

from numba.experimental import jitclass 
from numba import int32, float32    # import the types
from numba.typed import List as NumbaList
import numba

spec = [
    ('cand_d', int32),
    ('pairs_num', int32),
    ('gene_opt_prob', float32)
]

@jitclass(spec)
class MyCrossover:
    
    def __init__(self, dimension: int, crossover_pairs: int, 
                 crossover_gene_operation_prob: float) -> None:
        self.cand_d: int = dimension
        self.pairs_num: int = crossover_pairs
        self.gene_opt_prob: float = crossover_gene_operation_prob

    def mate(self, population: List[List[float]], fitness: List[float]) -> List[float]:
        new_solutions = []
        for _ in range(self.pairs_num):
            cand1_idx, cand2_idx = -1, -1
            while True:
                cand1_idx = random.randint(0, len(population)-1)
                cand2_idx = random.randint(0, len(population)-1)
                if cand1_idx != cand2_idx:
                    break

            solution = []
            for g1, g2 in zip(population[cand1_idx], population[cand2_idx]):
                if random.uniform(0, 1) > self.gene_opt_prob:
                    # Дискретный кроссовер
                    solution.append(g1 if random.uniform(0,1) > 0.5 else g2)
                else:
                    # Арифметический кроссовер
                    lmbda = random.uniform(0, 1)
                    solution.append((lmbda * g1) + ((1 - lmbda) * g2))

            new_solutions.append(solution)

        return new_solutions

