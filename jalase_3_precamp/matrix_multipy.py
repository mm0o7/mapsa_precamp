from functools import reduce
def multiple_matrix(matrix1: list[list], matrix2: list[list]) ->list[list]:
    mat_ans = []
    if len(matrix2) == len(matrix1[0]):
        mat_ans = [[0 for x in range(len(matrix2[0]))]for y in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                mat_ans[i][j] = reduce(lambda a, b: a+ b, map(int, map(lambda x, y: x*y, map(int, matrix1[i]), [matrix2[k][j] for k in range(len(matrix1)+1)])))
    return mat_ans


mat1 = [[1,2,3],[4,5,6]]
mat2 = [[1],[2],[3]]
print(multiple_matrix(mat1, mat2))