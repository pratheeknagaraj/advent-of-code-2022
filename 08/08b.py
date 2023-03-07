#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

grid = []

for l in lines:
    grid.append([int(i) for i in list(l.strip())])

x = len(grid)
y = len(grid[0])

def get_scenic_score(i, j):
    height = grid[i][j]

    count_1 = 0
    for a in range(i+1, x):
        count_1 += 1
        if grid[a][j] >= height:
            break

    count_2 = 0
    for a in range(i-1, -1, -1):
        count_2 += 1
        if grid[a][j] >= height:
            break

    count_3 = 0
    for b in range(j+1, y):
        count_3 += 1
        if grid[i][b] >= height:
            break

    count_4 = 0
    for b in range(j-1, -1, -1):
        count_4 += 1
        if grid[i][b] >= height:
            break

    return count_1 * count_2 * count_3 * count_4

max_score = -1
for i in range(1, x-1):
    for j in range(1, y-1):
        score = get_scenic_score(i, j)
        max_score = max(score, max_score)

print(max_score)

