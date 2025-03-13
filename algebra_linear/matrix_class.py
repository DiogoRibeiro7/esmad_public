from typing import List


class Matrix:
    def __init__(self, data: List[List[float]]) -> None:
        """
        Inicializa uma matriz com os dados fornecidos.

        Parâmetros:
            data: Uma lista de listas contendo números (float).
        """
        # Verifica se todas as linhas têm o mesmo comprimento
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Todas as linhas devem ter o mesmo comprimento.")

        # Atributos da classe
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Soma duas matrizes.

        Parâmetros:
            other: Outra matriz para ser somada.

        Retorna:
            Uma nova matriz contendo a soma.
        """
        # Verifica se as matrizes têm as mesmas dimensões
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("As matrizes precisam ter as mesmas dimensões para serem somadas.")

        # Calcula a soma elemento a elemento
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def scalar_multiply(self, scalar: float) -> 'Matrix':
        """
        Multiplica a matriz por um escalar.

        Parâmetros:
            scalar: Valor numérico pelo qual multiplicar a matriz.

        Retorna:
            Uma nova matriz multiplicada pelo escalar.
        """
        # Multiplica cada elemento pelo escalar
        result = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def dot_product(self, other: 'Matrix') -> 'Matrix':
        """
        Realiza o produto interno (multiplicação matricial).

        Parâmetros:
            other: A segunda matriz para realizar o produto interno.

        Retorna:
            Uma nova matriz resultante do produto interno.
        """
        # Verifica condições para multiplicação matricial
        if self.cols != other.rows:
            raise ValueError("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")

        # Calcula o produto interno
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def cross_product(self, other: 'Matrix') -> 'Matrix':
        """
        Realiza o produto vetorial entre dois vetores tridimensionais.

        Parâmetros:
            other: Outro vetor tridimensional.

        Retorna:
            Um novo vetor resultante do produto vetorial.
        """
        # Verifica se são vetores coluna tridimensionais
        if self.rows != 3 or self.cols != 1 or other.rows != 3 or other.cols != 1:
            raise ValueError("Produto vetorial é definido apenas para vetores coluna tridimensionais.")

        a = [self.data[i][0] for i in range(3)]
        b = [other.data[i][0] for i in range(3)]

        # Calcula o produto vetorial
        result = [
            [a[1]*b[2] - a[2]*b[1]],
            [a[2]*b[0] - a[0]*b[2]],
            [a[0]*b[1] - a[1]*b[0]]
        ]

        return Matrix(result)

    def __repr__(self) -> str:
        """
        Retorna representação em string da matriz.
        """
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


# Demonstração prática da classe Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("Soma das matrizes A e B:")
print(A + B)

print("\nMatriz A multiplicada por escalar 2:")
print(A.scalar_multiply(2))

print("\nProduto interno das matrizes A e B:")
print(A.dot_product(B))

print("\nProduto vetorial dos vetores v1 e v2:")
v1 = Matrix([[1], [0], [0]])
v2 = Matrix([[0], [1], [0]])
print(v1.cross_product(v2))

