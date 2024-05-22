import typing
from typing import List
import random
import numpy as np
from copy import deepcopy, copy

from numba.experimental import jitclass 
from numba import int32, float32    # import the types
from numba.typed import List as NumbaList

spec = [
    ('pop_size', int32)
]

@jitclass(spec)
class MySelector:
    def __init__(self, population_size: int) -> None:
        self.pop_size: int = population_size

    def filter_population(self, population: List[List[float]], fitnesses: List[float]) -> List[List[float]]:
        sorted_fitnesess = sorted([[float(i), fit] for i, fit in zip(range(len(population)), fitnesses)], 
                                  key=lambda p: p[1], reverse=True)[:self.pop_size]
        
        selected_pop = [population[int(i)] for i, _ in sorted_fitnesess]

        return selected_pop