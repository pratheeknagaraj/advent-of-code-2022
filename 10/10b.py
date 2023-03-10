#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

register = 1

cycle = 1

for line in lines:
    l = line.strip()

    spin = 0
    val = 0

    if l.startswith('noop'):
        spin = 1
    elif l.startswith('addx'):
        val = int(l.split()[1])
        spin = 2

    for i in range(spin):
        cycle_pos = (cycle-1) % 40
        if cycle_pos in (register-1, register, register+1):
            print('#', end="")
        else:
            print('.', end="")

        if cycle in (40, 80, 120, 160, 200, 240):
            print()

        cycle += 1

    register += val
