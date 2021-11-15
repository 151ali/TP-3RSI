import numpy as np
from utils import DFS
class CMTD:
    def __init__(
        self, E 
    ):
        self.E = E # espace d'etats

    def setInitial(self, initial):
        # size 
        if initial.shape[0] != self.E :
            raise Exception("initial vector must be same as |"+str(self.E)+"|")
            
        else:
            self.initial = initial
            # proba dist
            if initial.sum() != 1.0:
                raise Exception("initail vector must be a proba distribution")
                

    def setTransitions(self, transitions):
        # squered matrix (E, E)
        if transitions.shape != (self.E,self.E):
            raise Exception("transition matrix P must have shape of ("+str(self.E)+","+str(self.E)+")")
            
        else:
            self.transitions = transitions
            # some of a row = 1
            
            for i in range(self.E):
                tr = self.transitions[i]
                row = tr.sum()

                for j in range(self.E):
                    if tr[j] < 0: # + > 1
                        raise Exception("negative value at line "+ str(i) +" column "+ str(j))
                
                if row != 1.0:
                    raise Exception("the sum of row " +str(i)+" must be 1, found " + str(row))

                
    def generate(self,initial,n):
        """
        make n step from a given initaial state
        """
        if n < 0:
            print("n must be >= 0")
            exit(1)
        else:
            state = initial
            #print(state)
            for i in range(0,n):
                state = state.dot(self.transitions)

            print("Initial state : " + str(initial) + " ->  " + str(state))

    def simulation_stochastique(self, taille):
        initStates = np.identity(self.E)
        for i in range(self.E):
            self.generate(initStates[i],taille)


    def isIrreductible(self):
        
        for start in range(self.E):
            visited = [False] * self.E
            DFS(self.transitions, start, visited)
            if False in visited:
                return False
        return True
        
    def __repr__(self):
        pass