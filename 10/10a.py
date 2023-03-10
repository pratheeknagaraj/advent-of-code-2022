#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

register = 1

cycle = 1

strength = 0

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
        if cycle in (20, 60, 100, 140, 180, 220):
            strength += cycle * register
        cycle += 1

    register += val

print(strength)
