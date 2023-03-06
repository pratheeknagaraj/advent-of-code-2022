#!/usr/bin/python3

with open('05_input', 'r') as f:
    lines = f.readlines()

stacks = {}
moves = []

is_move = False
split_len = 4

for line in lines:
    if line.strip() == '':
        is_move = True
        continue

    if is_move:
        moves.append(line.strip())
    else:
        if '[' not in line:
            continue
        buckets = [(i, line[i:i+split_len]) for i in range(0, len(line), split_len)]
        for b in buckets:
            pos = b[0] // split_len + 1
            let = b[1]
            if let.strip() == '':
                continue
            else:
                l = let.strip()[1]
                stacks[pos] = stacks.get(pos, [])
                stacks[pos].append(l)


for move in moves:
    parts = move.strip().split()
    n = int(parts[1])
    start = int(parts[3])
    end = int(parts[5])

    boxes = stacks[start][:n]
    stacks[start] = stacks[start][n:]
    stacks[end] = boxes + stacks[end]

letter_string = ''
for p in sorted(stacks.keys()):
    letter_string += stacks[p][0]

print(letter_string)
