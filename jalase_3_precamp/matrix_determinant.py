def deleted_matrix(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

def matrix_deternminant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for i in range(len(matrix)):
        determinant += ((-1) ** i) * matrix[0][i]* matrix_deternminant(deleted_matrix(matrix, 0, i))
    return determinant