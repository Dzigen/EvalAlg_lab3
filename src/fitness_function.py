import typing
from typing import List
from math import pi, cos, exp, sqrt
import random

from numba.experimental import jitclass 
from numba import int32, float32    # import the types
spec = [
    ('cand_d', int32),
    ('best_result', float32),
    ('global_optimum', float32)
]

@jitclass(spec)
class FitnessFunction:
    
    def __init__(self, dimension: int) -> None:
        self.cand_d: int = dimension
        self.best_result: float = 0
        self.global_optimum: float = 10

    def calculate_fitness(self, solution: List[float]) -> float:
        n: int = self.cand_d
        dn: float = 1.0 / n
        a: float = 10
        b: float = 0.2
        c: float = 2 * pi
        s1: float = 0.0
        s2: float = 0.0
        
        for i in range(self.cand_d):
            val: float = solution[i] + random.random()
            s1 += val * val
            s2 += cos(c * val)
        
        s1 = -a * exp(-b * sqrt(dn * s1))
        s2 = -exp(dn * s2)
        result: float = s1 + s2 + a + exp(1)
        result = -result
        result += a
        result = abs(result)

        if self.best_result < result:
            self.best_result = result
        
        return result