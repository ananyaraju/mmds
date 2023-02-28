mat = [ 
 [0, 1], 
 [-2, -3] 
] 
 
# calculate eigenvalues and eigenvectors
 
# solve quadratic equation for "lambda"
a = 1
b = -(mat[0][0] + mat[1][1]) 
c = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0] 
 
#values of lambda
x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a) 
x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a) 
 
eigenvalues = [x1, x2] 
print(eigenvalues) 
 
# for lambda 1:
mat_x1 = [[mat[0][0] - x1, mat[0][1]], [mat[1][0], mat[1][1] - x1]] 
eig_x1 = [[-mat_x1[0][1]], [mat_x1[0][0]]] 
print(eig_x1) 
 
# for lambda 2:
mat_x2 = [[mat[0][0] - x2, mat[0][1]], [mat[1][0], mat[1][1] - x2]] 
eig_x2 = [[-mat_x2[0][1]], [mat_x2[0][0]]] 
print(eig_x2) 
 
# [original matrix][eigenvector matrix] = [eigenvector matrix][eigenvalue matrix]
eigen_vec_mat = [[eig_x1[0][0], eig_x2[0][0]], [eig_x1[1][0], eig_x2[1][0]]] 
eigen_val_mat = [[x1, 0], [0, x2]] 
 
# check
print(mat) 
print(eigen_vec_mat) 
print(eigen_val_mat) 