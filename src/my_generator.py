import typing
from typing import List, Dict
import random

from numba.experimental import jitclass 
from numba import int32, float32     # import the types
from numba.typed import List as NumbaList
import math

spec = [
    ('cand_d', int32),
    ('pop_mltply', int32),
    ('gen_mode', int32)
]

@jitclass(spec)
class MyGenerator:

    def __init__(self, dimension: int, gen_mode: int, over_pop_multiply: int = 5) -> None:
        self.cand_d: int = dimension
        self.pop_mltply: int = over_pop_multiply
        self.gen_mode: int = gen_mode

    def gen_random_solution(self) -> List[float]:
        return [random.uniform(-5, 5) for _ in range(self.cand_d)]
    
    def dist(self, p1: List[float], p2: List[float]) -> float:
        return math.sqrt(sum([math.pow(v1-v2,2) for v1, v2 in zip(p1,p2)]))
    
    def get_population(self, pop_size: int) -> List[List[float]]:
        if self.gen_mode == 0: # 'uniform'
            return [self.gen_random_solution() for _ in range(pop_size)]
        
        elif self.gen_mode == 1: # 'max_dist'
            over_size = pop_size * self.pop_mltply 
            over_pop = [self.gen_random_solution() for _ in range(over_size)]

            distances = []
            #med_pi = over_size // 2
            for i, point_anchor in enumerate(over_pop):
                #med_dist = sorted([self.dist(point_anchor, point_neighbor) for j, point_neighbor in enumerate(over_pop)])[med_pi]
                min_dist = min([self.dist(point_anchor, point_neighbor) for j, point_neighbor in enumerate(over_pop) if j!=i])
                distances.append(min_dist)

            ranged_points = sorted(list(zip(distances, list(range(over_size)))), 
                                key=lambda v: v[0], reverse=True)[:pop_size]

            selected_points = []
            for d, i in ranged_points:
                selected_points.append(over_pop[i])

            return selected_points
        
        elif self.gen_mode == 2: # 'bordered'
            return [[5.0 if random.uniform(0,1) > 0.5 else -5.0 for _ in range(self.cand_d)] for _ in range(pop_size)]
        
        else:
            raise KeyError
