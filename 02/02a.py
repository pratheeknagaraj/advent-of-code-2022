#!/usr/bin/python3

with open('02_input', 'r') as f:
    lines = f.readlines()

total_score = 0

for l in lines:
    opponent, me = l.strip().split()

    shape_score = 0
    if me == 'X':
        shape_score = 1
    elif me == 'Y':
        shape_score = 2
    elif me == 'Z':
        shape_score = 3

    outcome_score = 0
    if opponent == 'A':
        if me == 'X':
            outcome_score = 3
        elif me == 'Y':
            outcome_score = 6
    elif opponent =='B':
        if me == 'Y':
            outcome_score = 3
        elif me == 'Z':
            outcome_score = 6
    elif opponent == 'C':
        if me == 'Z':
            outcome_score = 3
        elif me == 'X':
            outcome_score = 6

    combined_score = shape_score + outcome_score

    total_score += combined_score

print(total_score)
