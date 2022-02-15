def eigen_matrix(matrix: list[list], landa = None) ->list[list]:
    mat_ans = [[0 for x in range(len(matrix))]for y in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                mat_ans[i][j] == matrix[i][j] - landa
            else:
                mat_ans[i][j] == matrix[i][j]
        
def deleted_matrix(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

def matrix_deternminant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for i in range(len(matrix)):
        determinant += ((-1) ** i) * matrix[0][i]* matrix_deternminant(deleted_matrix(matrix, 0, i))
    return determinant    
        
def calulate_eigenvalue(matrix: list[list]) ->int:
    i = matrix_deternminant(eigen_matrix(matrix))
    return i
    
mat = [[2, -4],[-1, -1]]
calulate_eigenvalue(mat)    