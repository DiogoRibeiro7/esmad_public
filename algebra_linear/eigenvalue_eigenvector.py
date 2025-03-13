from typing import List, Tuple


def dot_product(v1: List[float], v2: List[float]) -> float:
    """Calcula o produto escalar entre dois vetores."""
    return sum(x * y for x, y in zip(v1, v2))


def matrix_vector_product(matrix: List[List[float]], vector: List[float]) -> List[float]:
    """Calcula o produto de uma matriz por um vetor."""
    return [dot_product(row, vector) for row in matrix]


def vector_norm(v: List[float]) -> float:
    """Calcula a norma Euclidiana (magnitude) de um vetor."""
    return sum(x**2 for x in v) ** 0.5


def normalize_vector(v: List[float]) -> List[float]:
    """Normaliza um vetor."""
    norm = vector_norm(v)
    if norm == 0:
        raise ValueError("Vetor nulo não pode ser normalizado.")
    return [x / norm for x in v]


def power_method(matrix: List[List[float]], iterations: int = 1000, tol: float = 1e-10) -> Tuple[float, List[float]]:
    """
    Calcula o maior autovalor em módulo e seu autovetor usando o método das potências.

    Parâmetros:
        matrix: Matriz quadrada arbitrária.
        iterations: Número máximo de iterações.
        tol: Tolerância para convergência.

    Retorna:
        Uma tupla contendo o maior autovalor e o autovetor correspondente.

    Exceções:
        ValueError: Caso a matriz não seja quadrada ou o método não convirja.
    """
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("A matriz precisa ser quadrada.")

    # Inicialização com vetor inicial arbitrário
    b_k = [1.0] * n

    for _ in range(iterations):
        # Multiplicação matriz-vetor
        b_k1 = matrix_vector_product(matrix, b_k)

        # Normalização
        b_k1_norm = vector_norm(b_k1)
        if b_k1_norm == 0:
            raise ValueError("Convergência impossível: matriz singular ou vetor inicial inadequado.")

        b_k_next = [x / b_k1_norm for x in b_k1]

        # Verificação de convergência
        if vector_norm([b_next - b_curr for b_next, b_curr in zip(b_k_next, b_k)]) < tol:
            break

        b_k = b_k_next

    eigenvalue = dot_product(matrix_vector_product(matrix, b_k), b_k)
    eigenvector = b_k

    return eigenvalue, eigenvector



matriz = [
    [4, 1, 2],
    [1, 3, 1],
    [2, 1, 3]
]

valor, vetor = power_method(matriz)

print("Maior Autovalor:", valor)
print("Autovetor Correspondente:", vetor)
