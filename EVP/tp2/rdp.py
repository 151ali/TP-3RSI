import numpy as np

class RdP:
    def __init__(self,nP,nT):
        self.nP = nP
        self.nT = nT

    
    def setArgs(
        self,
        C_plus,
        C_minus,
        M0
    ):
    
        if np.any(M0 < 0) or np.any(C_minus < 0) or np.any(C_plus < 0):
            raise  Exception("negative values not permitted")

        if C_plus.shape != (self.nP, self.nT) or C_minus.shape != (self.nP, self.nT):
            raise Exception("C+ and C- must have shape (nP, nT)")

        if M0.shape != (self.nP,):
            raise Exception("M0 must have shape (nP,)")


        self.C_plus  = C_plus
        self.C_minus = C_minus
        self.M0      = M0

        self.C = C_plus - C_minus
    
    def tirable(self, M, t):
        # M >= C-(., t)
        return np.all(M >=self.C_minus[:,t])

    def haja(self, newM, oldM):
        return np.all(newM >= oldM) and np.any(newM > oldM)

    def isBounded(self):
    
        checked = []
        pending = [self.M0]
        
        while pending != []:

            # chek if it already checked
            M = pending.pop(0)
            M_in_checked = False
            for item in checked:
                if (np.all(item == M)):
                    M_in_checked = True
                    break

            if not M_in_checked:
                checked.append(M)
                for t in range(self.nT):
                    if self.tirable(M, t=t):
                        newM = M + self.C[:,t]
                        print(f"{M} ---> {newM}")
                        pending.append(newM)
                        
                    
                        if( self.haja(newM, M) ):
                            print("--- not bounded ---")
                            return False
                    
        print(f"bounded with |A| = {len(checked)}")
        return True


def test():
    C_minus  = np.array([[3, 0], [1, 1], [0, 1], [0, 0]])
    C_plus = np.array([[0, 0], [1, 1], [0, 0], [1, 2]])    
    M0      = np.array([4, 1, 2, 0])


    rdp = RdP(nP=4,nT=2)
    rdp.setArgs(C_plus, C_minus, M0)
    rdp.isBounded()


if __name__=="__main__":
    test()