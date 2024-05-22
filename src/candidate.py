import typing
from typing_extensions import List
from dataclasses import dataclass

#from numba.experimental import jitclass 
#from numba import int32, float32    # import the types
#spec = [
#    ('solution', float32[:]),
#    ('fitness', float32)
#]

@dataclass
class Candidate:
    solution: List[float] = None
    fitness: float = 0
        