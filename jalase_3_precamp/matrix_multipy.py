from functools import reduce
def multiple_matrix(matrix1: list[list], matrix2: list[list]) ->list[list]:
    a = []
    #a.append(reduce(lambda a, b: a+ b, map(lambda x, y: x*y, map(list, matrix1), map(list, map(list, matrix2)))))
    #print(list(map(lambda x, y: x*y, map(list, matrix1), map(list, map(list, matrix2)))))
    print(list(map(list, map(list, matrix2))))
    print(list(map(list, matrix1)))
    return a
mat1 = [[1, 2, 3],[4, 5, 6]]
mat2 = [[1],[2],[3]]
print(multiple_matrix(mat1, mat2))