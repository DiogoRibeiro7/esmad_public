from typing import List

def determinant(matrix: List[List[float]]) -> float:
    """
    Calculates the determinant of a square matrix using cofactor expansion.

    Parameters:
    matrix (List[List[float]]): Square matrix represented as a list of lists.

    Returns:
    float: Determinant value.

    Raises:
    ValueError: If the matrix is not square.
    """
    # Verify if the matrix is square
    rows = len(matrix)
    if any(len(row) != rows for row in matrix):
        raise ValueError("The matrix must be square.")

    # Base case for 1x1 matrix
    if rows == 1:
        return matrix[0][0]

    # Base case for 2x2 matrix
    if rows == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive case for larger matrices
    det = 0
    for col in range(rows):
        # Create submatrix excluding row 0 and current column
        submatrix = [
            [matrix[i][j] for j in range(rows) if j != col]
            for i in range(1, rows)
        ]
        # Calculate cofactor and add to total determinant
        cofactor = ((-1) ** col) * matrix[0][col]
        det += cofactor * determinant(submatrix)

    return det


example_matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

result = determinant(example_matrix)
print(f"Determinant: {result}")
