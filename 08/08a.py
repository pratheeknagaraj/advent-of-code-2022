#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

grid = []

for l in lines:
    grid.append([int(i) for i in list(l.strip())])

x = len(grid)
y = len(grid[0])

visible_grid = set()

for i in range(x):
    max_height = grid[i][0]
    visible_grid.add((i,0))
    for j in range(1, y):
        if grid[i][j] > max_height:
            visible_grid.add((i,j))
            max_height = grid[i][j]

for i in range(x):
    max_height = grid[i][y-1]
    visible_grid.add((i,y-1))
    for j in range(y-2, -1, -1):
        if grid[i][j] > max_height:
            visible_grid.add((i,j))
            max_height = grid[i][j]

for j in range(y):
    max_height = grid[0][j]
    visible_grid.add((0,j))
    for i in range(1, x):
        if grid[i][j] > max_height:
            visible_grid.add((i,j))
            max_height = grid[i][j]

for j in range(y):
    max_height = grid[x-1][j]
    visible_grid.add((x-1,j))
    for i in range(x-1, -1, -1):
        if grid[i][j] > max_height:
            visible_grid.add((i,j))
            max_height = grid[i][j]

print(len(visible_grid))
