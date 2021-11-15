import numpy as np
from cmtd import  CMTD

transitions = np.array([
    [1/3, 1/3, 1/3],
    [3/4, 0, 1/4],
    [.5, 0, .5]
])


chaine = CMTD(3)
chaine.setTransitions(transitions)
#chaine.simulation_stochastique(3)
print(chaine.isIrreductible())
