from typing import List

def multiplica_matrizes(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiplica duas matrizes A e B sem usar numpy.
    
    Parâmetros:
    A (List[List[float]]): Primeira matriz de dimensões (m, n).
    B (List[List[float]]): Segunda matriz de dimensões (n, p).
    
    Retorna:
    List[List[float]]: Matriz resultante da multiplicação AxB de dimensões (m, p).
    
    Lança:
    ValueError: Se as dimensões das matrizes forem incompatíveis para multiplicação.
    """
    # Verifica se as matrizes não estão vazias e são bem formadas
    if not A or not B or not all(isinstance(row, list) for row in A) or not all(isinstance(row, list) for row in B):
        raise ValueError("As matrizes devem ser listas de listas não vazias.")

    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])

    # Verifica se todas as linhas têm o mesmo número de colunas
    if any(len(row) != num_colunas_A for row in A) or any(len(row) != num_colunas_B for row in B):
        raise ValueError("Todas as linhas da matriz devem ter o mesmo número de colunas.")

    # Verifica a compatibilidade das dimensões para multiplicação
    if num_colunas_A != num_linhas_B:
        raise ValueError(f"Incompatibilidade de dimensões: {num_colunas_A} ≠ {num_linhas_B}")

    # Inicializa a matriz resultante com zeros
    C = [[0.0 for _ in range(num_colunas_B)] for _ in range(num_linhas_A)]

    # Multiplicação de matrizes
    for i in range(num_linhas_A):
        for j in range(num_colunas_B):
            soma = 0.0
            for k in range(num_colunas_A):  # ou num_linhas_B, que são iguais
                soma += A[i][k] * B[k][j]
            C[i][j] = soma
    
    return C

# Exemplo de uso:
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

resultado = multiplica_matrizes(A, B)

# Exibir o resultado de forma organizada
for linha in resultado:
    print(linha)
