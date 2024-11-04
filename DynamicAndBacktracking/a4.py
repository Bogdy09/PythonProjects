# A player at `PRONOSPORT` wants to choose score options for four games. The options may be `1`, `X`, `2`. Generate all possible alternatives, knowing that:
#- The last score option may not be `X`
#- There should be no more than two score options of `1`


def generate_scores_iterative():
    stack = [(0, [], 0)]  # Initialize the stack with the initial state: index, current score, and ones_count.
    scores = []  # Store valid score alternatives.

    while stack:
        index, current, ones_count = stack.pop()  # Get the current state from the stack.

        if index == 4:
            if ones_count <= 2 and current[-1] != 'X':
                scores.append(current)  # If we have generated a complete score alternative, add it to the results.
        else:
            for option in ['1', 'X', '2']:
                new_score = current + [option]  # Generate a new score alternative by appending '1', 'X', or '2'.
                new_ones_count = ones_count + (1 if option == '1' else 0)  # Update ones_count if '1' is added.

                if new_ones_count <= 2:
                    stack.append((index + 1, new_score, new_ones_count))  # Add the new state to the stack for further exploration.

    return scores

scores = generate_scores_iterative()

for score in scores:
    print(" ".join(score))  # Print each valid score option.

print("Number of solutions:", len(scores))  # Print the total number of valid solutions.
