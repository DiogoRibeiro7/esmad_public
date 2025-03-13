from typing import List, Tuple


def gaussian_elimination(matrix: List[List[float]], 
                         vector: List[float]) -> List[float]:
    """
    Resolve um sistema linear Ax = b usando eliminação gaussiana
    com substituição retroativa.

    Parâmetros:
        matrix: Matriz quadrada de coeficientes (A).
        vector: Vetor de termos independentes (b).

    Retorna:
        Vetor solução x do sistema Ax = b.

    Exceções:
        ValueError: Caso o sistema não possua solução única.
    """
    n = len(matrix)

    # Validações
    if any(len(row) != n for row in matrix):
        raise ValueError("A matriz deve ser quadrada.")
    if len(vector) != n:
        raise ValueError("Dimensão do vetor deve ser igual à da matriz.")

    # Matriz aumentada
    for i in range(n):
        matrix[i].append(vector[i])

    # Eliminação gaussiana
    for i in range(n):
        # Pivotamento parcial
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        pivot = matrix[i][i]
        if abs(pivot) < 1e-12:
            raise ValueError("Sistema não tem solução única.")

        # Normalização da linha do pivô
        for k in range(i, n + 1):
            matrix[i][k] /= pivot

        # Zerando elementos abaixo do pivô
        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Substituição retroativa
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] - sum(matrix[i][j] * x[j] for j in range(i + 1, n))

    return x



A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

b = [8.0, -11.0, -3.0]

solution = gaussian_elimination(A, b)

print("Solução:", solution)
