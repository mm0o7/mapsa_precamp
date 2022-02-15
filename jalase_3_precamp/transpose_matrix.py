from ast import Return


def transpose(matrix: list[list]) ->list[list]:
    transpose_matrix = [i for i in zip(*matrix)]
    return transpose_matrix
