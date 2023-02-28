#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

elves = []
cur_elf = []
for l in lines:
    s = l.strip()
    if s is '':
        elves.append(cur_elf)
        cur_elf = []
    else:
        cur_elf.append(int(s))

elves.append(cur_elf)

max_calories = max([sum(e) for e in elves])

print(max_calories)
