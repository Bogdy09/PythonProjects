#Given an `n * n` square matrix with integer values, find the maximum length of a snake sequence.
# A snake sequence begins on the matrix's top row (coordinate `(0, i), 0 <= i < n`).
# Each element of the sequence, except the first one, must have a value `±1` from the previous one
# and be located directly below, or directly to the right of the previous element.
# For example, element `(i, j)` can be succeded by one of the `(i, j + 1)` or `(i + 1, j)` elements.
# Display the length as well as the sequence of coordinates for one sequence of maximum length.

def snakesequence(S, m, n):
    # Initialize a dictionary to store the sequence and its coordinates
    sequence = {}

    # Create a matrix for dynamic programming, all initialized to 1
    DP = [[1 for x in range(m + 1)] for x in range(n + 1)]

    # Initialize variables for value comparisons and position tracking
    a, b, maximum = 0, 0, 0
    position = [0, 0]

    # Loop through rows and columns of the matrix
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            a, b = 0, 0
            p = "initial"

            # Check if moving upwards is possible and the difference in values is 1
            if (i > 0 and abs(S[i][j] - S[i - 1][j]) == 1):
                a = DP[i - 1][j]

            # Check if moving leftwards is possible and the difference in values is 1
            if (j > 0 and abs(S[i][j] - S[i][j - 1]) == 1):
                b = DP[i][j - 1]

            # Determine the path to the current cell based on maximum value
            if a != 0 and a >= b:
                p = str(i - 1) + " " + str(j)
            elif b != 0:
                p = str(i) + " " + str(j - 1)
            q = str(i) + " " + str(j)

            # Store the path to the current cell in the sequence dictionary
            sequence[q] = p

            # Update the dynamic programming array with the maximum sequence length
            DP[i][j] = DP[i][j] + max(a, b)

            # Update the maximum sequence and its position
            if DP[i][j] >= maximum:
                maximum = DP[i][j]
                position[0] = i
                position[1] = j

    #tracing and constructing snake sequence
    # Initialize lists to store snake values and positions
    snakeValues = []
    snakePositions = []

    # Add the initial snake value based on the maximum position
    snakeValues.append(S[position[0]][position[1]] ) #add first nr of snake sequence
    check = 'found'
    str_next = str(position[0]) + " " + str(position[1]) #current position
    findingIndices = sequence[str_next].split()

    # Trace back to construct the snake sequence
    while (check == 'found'):
        if sequence[str_next] == 'initial':
            snakePositions.insert(0, str_next)
            check = 'end'
            continue
        findingIndices = sequence[str_next].split()#we split one piece for the row one for column
        g = int(findingIndices[0]) #for the row
        h = int(findingIndices[1]) #for the column
        snakeValues.insert(0, S[g][h]) #add the value from the matrix
        snake_position = str(g) + " " + str(h)
        snakePositions.insert(0, str_next)
        str_next = sequence[str_next] #update current instruction

    # Print the DP array
    print("Dynamic Programming Array (DP):")
    for row in DP:
        print(row)

    return [snakeValues, snakePositions]

# Define the input matrix and its dimensions
S = [[9, 6, 5, 2],
     [8, 7, 6, 5],
     [7, 3, 1, 6],
     [1, 1, 10, 7]]
m = 3
n = 3

# Find the snake sequence
seq = snakesequence(S, m, n)

# Print the snake sequence values and their coordinates
for i in range(len(seq[0])):
    print(seq[0][i], ",", seq[1][i].split())
