import numpy as np
from numpy.linalg import eig

r = int(input("Number of rows in matrix: "))
c = int(input("Number of cols in matrix: "))

if (r!=c):
    print("only square matrices are valid\n")
else:
    m = []
    print("\nenter matrix data")
    for x in range(r):
        col = []
        for y in range(c):            
            val = int(input("a["+str(x)+"]["+str(y)+"] = "))
            col.append(val)
        m.append(col)
    print("\nmatrix: ")
    print(m)
    
    a = np.array(m)
    eigenvalue,eigenvector = eig(a)
    print("\neigenvalues = ",eigenvalue)
    print("\neigenvectors = \n",eigenvector)