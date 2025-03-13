from typing import List

def matrix_inverse(matrix: List[List[float]]) -> List[List[float]]:
    if len(matrix) != len(matrix[0]):
        raise ValueError("A matriz precisa ser quadrada para ter inversa.")

    n = len(matrix)
    identity = [[float(i == j) for j in range(n)] for i in range(n)]
    augmented = [matrix[i] + identity[i] for i in range(n)]

    for i in range(n):
        pivot = augmented[i][i]
        if abs(pivot) < 1e-12:
            raise ValueError("A matriz não é inversível.")

        augmented[i] = [x / pivot for x in augmented[i]]

        for j in range(n):
            if j != i:
                factor = augmented[j][i]
                augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(2*n)]

    return [row[n:] for row in augmented]


A = [[4, 7, 3], [2, 6, 1], [2, 3, 1]]


print("\nInversa da matriz A:")
try:
    inv_A = matrix_inverse(A)
    print(inv_A)
except ValueError as e:
    print("Erro:", e)