from typing import List

def eliminacao_de_gauss(A: List[List[float]], b: List[float]) -> List[float]:
    """
    Resolve um sistema linear Ax = b usando o método de eliminação de Gauss.
    
    Parâmetros:
    A (List[List[float]]): Matriz de coeficientes do sistema (n x n).
    b (List[float]): Vetor de termos independentes (n).
    
    Retorna:
    List[float]: Vetor solução x (n).
    
    Lança:
    ValueError: Se a matriz A não for quadrada ou se houver inconsistência nos tamanhos.
    """
    n = len(A)

    # Verifica se a matriz é quadrada e se o vetor b tem dimensão correta
    if any(len(row) != n for row in A) or len(b) != n:
        raise ValueError("A matriz A deve ser quadrada e o vetor b deve ter o mesmo número de linhas.")

    # Construindo a matriz aumentada [A | b]
    for i in range(n):
        A[i].append(b[i])

    # Fase de eliminação
    for i in range(n):
        # Pivotamento parcial (opcional, mas melhora estabilidade numérica)
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if A[max_row][i] == 0:
            raise ValueError("O sistema não tem solução única (matriz singular).")
        A[i], A[max_row] = A[max_row], A[i]

        # Normalizando a linha pivô
        pivô = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= pivô
        
        # Zerando os elementos abaixo do pivô
        for k in range(i + 1, n):
            fator = A[k][i]
            for j in range(i, n + 1):
                A[k][j] -= fator * A[i][j]

    # Fase de substituição regressiva
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    
    return x

# Exemplo de uso:
A = [[2, -1, 1], 
     [1, 3, 2], 
     [1, -1, 2]]
b = [8, 13, 3]

solucao = eliminacao_de_gauss(A, b)

print("Solução do sistema:", solucao)
