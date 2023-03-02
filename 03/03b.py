#!/usr/bin/python3

with open('03_input', 'r') as f:
    lines = f.readlines()

def handle_lines(l1, l2, l3):
    i1 = set(list(l1.strip()))
    i2 = set(list(l2.strip()))
    i3 = set(list(l3.strip()))

    common = i1 & i2 & i3

    shared = list(common)[0]

    priority = get_priority(shared)

    return priority

def get_priority(c):
    return ord(c) - 38 if c.isupper() else ord(c) - 96

total = 0

i = 0

while i < len(lines):
    l1, l2, l3 = lines[i], lines[i+1], lines[i+2]
    p = handle_lines(l1, l2, l3)
    i += 3

    total += p

print(total)

