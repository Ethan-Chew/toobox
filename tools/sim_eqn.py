#by Jerick
import numpy as np
def solve_sim(*args):
    ''''
    args are the amount of equations, each of the equations are a list of numbers representing each variable
    e.g [10,4,9],[9,3,4] to represent 10x+4y=0, 9x+3y=4

    '''
    answermatrix=np.matrix([[i[-1]] for i in args],dtype=float)
    try:
        therestinvered=np.linalg.inv(np.matrix([i[:-1] for i in args],dtype=float))
    except:
        return "not possible"
    try:
        return (lambda x: [i[0] for i in x])(np.dot(therestinvered,answermatrix) )
    except:
        return "error"

if __name__ == "__main__":
    print(solve_sim([1,2,4],[3,-5,1]))
