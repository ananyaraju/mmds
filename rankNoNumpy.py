def matmul2(A, B): 
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B") 
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                C[i][j] += A[i][k] * B[k][j]
    return C 
 
def matmul3(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B") 
    C = [[0 for i in range(len(B[0]))] for j in range(len(A))] 
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                C[i][j] += A[i][k] * B[k][j] 
    return C 
 
def addmat(A, B): 
    if len(A) != len(B): 
        raise ValueError("Number of columns in A must equal number of rows in B") 
    C = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)): 
        for j in range(len(A[0])): 
            C[i][j] = A[i][j] + B[i][j] 
    return C 
 
def rank_of_mat(A): 
    B = [[0 for i in range(len(A[0]))] for j in range(len(A))] 
    for i in range(len(A)): 
        for j in range(len(A[0])): 
            B[i][j] = A[i][j] 
    rank = len(B)
    for i in range(rank): 
        if B[i][i] == 0: 
            for j in range(i+1, rank): 
                if B[j][i] != 0: 
                    B[i], B[j] = B[j], B[i] 
                    break
            else: 
                rank -= 1
                B[i], B[rank] = B[rank], B[i] 
                i -= 1
                continue
        for j in range(i+1, rank): 
            ratio = B[j][i] / B[i][i] 
            for k in range(rank): 
                B[j][k] = B[j][k] - ratio * B[i][k] 
    return rank 

A = [[1,1,1],[2,2,2],[3,3,3]]
C = [[1,2,3],[4,5,6],[7,8,9]]
print(matmul2(A,C))
print(matmul3(A,C))
print("add")
print(addmat(A,C))
print(rank_of_mat(A))
print(rank_of_mat(C))
