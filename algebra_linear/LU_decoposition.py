from typing import List, Tuple

def decomposicao_LU(A: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
    """
    Realiza a decomposição LU da matriz A.
    
    Parâmetros:
    A (List[List[float]]): Matriz quadrada de coeficientes (n x n).
    
    Retorna:
    Tuple[List[List[float]], List[List[float]]]: Matrizes L e U tal que A = LU.
    
    Lança:
    ValueError: Se A não for quadrada ou se for singular (det(A) = 0).
    """
    n = len(A)

    # Verifica se a matriz é quadrada
    if any(len(row) != n for row in A):
        raise ValueError("A matriz A deve ser quadrada.")

    # Inicializa L como matriz identidade e U como cópia de A
    L = [[0.0] * n for _ in range(n)]
    U = [[A[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        L[i][i] = 1  # Diagonal principal de L é 1

        for j in range(i + 1, n):
            if U[i][i] == 0:
                raise ValueError("A matriz é singular, decomposição LU não é possível.")

            fator = U[j][i] / U[i][i]
            L[j][i] = fator  # Guarda o multiplicador na matriz L

            for k in range(i, n):
                U[j][k] -= fator * U[i][k]  # Elimina o elemento abaixo do pivô

    return L, U


def resolve_sistema_LU(L: List[List[float]], U: List[List[float]], b: List[float]) -> List[float]:
    """
    Resolve o sistema Ax = b dado A = LU usando substituições diretas e regressivas.
    
    Parâmetros:
    L (List[List[float]]): Matriz triangular inferior (n x n).
    U (List[List[float]]): Matriz triangular superior (n x n).
    b (List[float]): Vetor de termos independentes (n).
    
    Retorna:
    List[float]: Vetor solução x.
    """
    n = len(L)

    # Substituição direta para resolver Ly = b
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    # Substituição regressiva para resolver Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x


# Exemplo de uso:
A = [[2, -1, 1], 
     [1, 3, 2], 
     [1, -1, 2]]
b = [8, 13, 3]

L, U = decomposicao_LU(A)
solucao = resolve_sistema_LU(L, U, b)

# Exibir resultados
print("Matriz L:")
for linha in L:
    print(linha)

print("\nMatriz U:")
for linha in U:
    print(linha)

print("\nSolução do sistema Ax = b:", solucao)
