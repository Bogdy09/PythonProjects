#Given an `n * n` square matrix with integer values, find the maximum length of a snake sequence.
# A snake sequence begins on the matrix's top row (coordinate `(0, i), 0 <= i < n`).
# Each element of the sequence, except the first one, must have a value `±1` from the previous one
# and be located directly below, or directly to the right of the previous element.
# For example, element `(i, j)` can be succeded by one of the `(i, j + 1)` or `(i + 1, j)` elements.
# Display the length as well as the sequence of coordinates for one sequence of maximum length.

def find_snake_sequence_naive(matrix, i, j, current_sequence):
    n = len(matrix)

    # If the current cell (i, j) is out of bounds, return the current sequence.
    if i < 0 or i >= n or j < 0 or j >= n:
        return current_sequence

    current_value = matrix[i][j]

    # Check if the current sequence is empty or if the current value can be part of the sequence.
    if not current_sequence or abs(current_value - current_sequence[-1][0]) == 1:
        current_sequence.append((current_value, (i, j)))

        # Explore two possible directions: right and down.
        right_sequence = find_snake_sequence_naive(matrix, i, j + 1, current_sequence.copy())
        down_sequence = find_snake_sequence_naive(matrix, i + 1, j, current_sequence.copy())

        # Return the longer sequence of the two.
        if len(right_sequence) > len(down_sequence):
            return right_sequence
        else:
            return down_sequence

    return current_sequence

# find the maximum snake sequence in the matrix
def find_maximum_snake_sequence(matrix):
    n = len(matrix)
    max_sequence = []

    # Iterate through all cells in the matrix as potential starting points for snake sequences.
    for i in range(n):
        for j in range(n):
            snake_sequence = find_snake_sequence_naive(matrix, i, j, [])
            if len(snake_sequence) > len(max_sequence):
                max_sequence = snake_sequence

    return max_sequence

matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 5, 3, 4],
    [4, 3, 2, 5]
]

snake_sequence = find_maximum_snake_sequence(matrix)
sequence_length = len(snake_sequence)

print("Maximum Snake Sequence:")
for value, (i, j) in snake_sequence:
    print(f"Value: {value}, Coordinates: ({i}, {j})")

print("Number of Elements in Maximum Sequence:", sequence_length)
