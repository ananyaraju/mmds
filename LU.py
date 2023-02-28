mat = [ 
 [1, 1, 1], 
 [3, 1, -3], 
 [1, -2, -5] 
] 
 
u11 = mat[0][0] 
u12 = mat[0][1] 
u13 = mat[0][2] 
 
l21 = mat[1][0] / u11 
u22 = mat[1][1] - l21 * u12 
u23 = mat[1][2] - l21 * u13 
 
l31 = mat[2][0] / u11 
l32 = (mat[2][1] - l31 * u12) / u22 
u33 = mat[2][2] - l31 * u13 - l32 * u23 
 
lower_triangular = [[1, 0, 0], [l21, 1, 0], [l31, l32, 1]] 
upper_triangular = [[u11, u12, u13], [0, u22, u23], [0, 0, u33]] 
 
print(lower_triangular) 
print(upper_triangular) 
