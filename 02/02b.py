#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

total_score = 0

for l in lines:
    opponent, me = l.strip().split()

    shape_score = None
    outcome_score = None

    if me == 'X':
        # Lose
        outcome_score = 0
        if opponent == 'A':
            shape_score = 3
        elif opponent == 'B':
            shape_score = 1
        elif opponent == 'C':
            shape_score = 2
    elif me == 'Y':
        # Draw
        outcome_score = 3
        if opponent == 'A':
            shape_score = 1
        elif opponent == 'B':
            shape_score = 2
        elif opponent == 'C':
            shape_score = 3
    elif me == 'Z':
        # Win
        outcome_score = 6
        if opponent == 'A':
            shape_score = 2
        elif opponent == 'B':
            shape_score = 3
        elif opponent == 'C':
            shape_score = 1

    combined_score = shape_score + outcome_score

    total_score += combined_score

print(total_score)
