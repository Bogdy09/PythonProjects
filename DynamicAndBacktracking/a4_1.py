# A player at `PRONOSPORT` wants to choose score options for four games. The options may be `1`, `X`, `2`. Generate all possible alternatives, knowing that:
#- The last score option may not be `X`
#- There should be no more than two score options of `1`

def generate_scores_recursive():
    options = ['1', 'X', '2']  # Available options
    n = 4  # Number of elements
    results = []  # Store valid alternatives

    # Recursive function to generate alternatives
    def backtrack(current_score, ones_count):
        if len(current_score) == n:
            if ones_count <= 2 and current_score[-1] != 'X':
                results.append(current_score)
            return

        for option in options:
            if option == '1':
                if ones_count < 2:
                    # Add '1' to the current alternative
                    backtrack(current_score + [option], ones_count + 1)
            else:
                # Add 'X' or '2' to the current alternative
                backtrack(current_score + [option], ones_count)

    backtrack([], 0)  # Start the backtracking

    return results

scores = generate_scores_recursive()
for score in scores:
    print(score)

print("Number of solutions:", len(scores))