from sympy import *

def eigen_value(matrix: list[list]) ->int:
    m_eigenvects = matrix.eigenvects()
    return m_eigenvects

print(eigen_value())
        
