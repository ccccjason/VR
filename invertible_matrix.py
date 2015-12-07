import numpy as np
from numpy import *
import numpy

def adjugate(matrix):  
    import numpy as np  
    C = np.zeros(matrix.shape) 
    nrows, ncols = C.shape    
    # Loop to calculate Cofactor  
    for row in xrange(nrows):  
        for col in xrange(ncols):  
            minor = matrix[np.array(range(row)+range(row+1,nrows))[:,np.newaxis],  
                           np.array(range(col)+range(col+1,ncols))]  
            C[row, col] = (-1)**(row+col) * np.linalg.det(minor) 
    return C.transpose() 

#A = mat([[3,5,1],[0,0,0],[2,0,0]])
A = mat([[1, -1 , -2],[2, -3 , -5],[-1,3,5]])
C = adjugate(A) / np.linalg.det(A)
print C



