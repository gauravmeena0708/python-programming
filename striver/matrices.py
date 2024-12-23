def matrix_rotate():
    def rotate_matrix(matrix):
        return [list(reversed(col)) for col in zip(*matrix)]

    # Example usage:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        print(row)

    rotated_matrix = rotate_matrix(matrix)
    for row in rotated_matrix:
        print(row)