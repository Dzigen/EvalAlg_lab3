import typing
import random
import numpy as np
from copy import deepcopy, copy
from typing import List, Dict

from numba.experimental import jitclass 
from numba import int32, float32    # import the types
from numba.typed import List as NumbaList
import numba

spec = [
    ('cand_d', int32),
    ('iterval_board', int32),
    ('gene_opt_prob', float32),
    ('gauss_sigma', float32),
    ('mutation_cand_prob', float32),
    ('mutation_gene_prob', float32),
    ('mode', int32)
]

@jitclass(spec)
class MyMutation:

    def __init__(self, dimension: int, mut_cand_prob: float, 
                 mut_gene_prob:float, mut_gene_opt_prob: float, 
                 gauss_sigma: float, mut_mode: int) -> None:
        self.cand_d: int = dimension
        self.iterval_board: int = 5
        self.mode = mut_mode
        
        self.gene_opt_prob: float = mut_gene_opt_prob
        self.gauss_sigma = gauss_sigma
        self.mutation_cand_prob: float = mut_cand_prob
        self.mutation_gene_prob: float = mut_gene_prob

    def apply(self, population: List[List[float]]) -> List[List[float]]:
        
        mutated_pop = [sol.copy() for sol in population]

        for c_idx in range(len(population)):
            # Случайно выбираем особь для мутации
            if random.uniform(0,1) < self.mutation_cand_prob:
                continue
            else:
                if self.mode == 1:
                    mutated_pop.append(population[c_idx].copy())
                    cur_c_idx = -1
                else:
                    cur_c_idx = c_idx

            for g_idx in range(self.cand_d):
                # Cлучайно выбираем ген особи для мутации
                if random.uniform(0,1) < self.mutation_gene_prob:
                    continue

                # Случайно выбираем оператор мутации
                updated_gene = None
                if random.uniform(0,1) > self.gene_opt_prob:
                    # Гауссова свёртка
                    while True:
                        updated_gene = mutated_pop[cur_c_idx][g_idx] + random.gauss(0, self.gauss_sigma)
                        if abs(updated_gene) <= self.iterval_board:
                            break
                else:
                    # Равномерная свёртка
                    while True:
                        updated_gene = mutated_pop[cur_c_idx][g_idx] + random.uniform(-5, 5)
                        if abs(updated_gene) <= self.iterval_board:
                            break
                
                # Обновляем ген у особи
                mutated_pop[cur_c_idx][g_idx] = updated_gene
            
        return mutated_pop