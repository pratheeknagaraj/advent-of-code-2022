#!/usr/bin/python3

with open('03_example_1', 'r') as f:
    lines = f.readlines()

def handle_line(line):
    l = line.strip()
    n = len(l)
    c1 = l[:n//2]
    c2 = l[n//2:]

    i1 = set(list(c1))
    i2 = set(list(c2))

    common = i1 & i2

    shared = list(common)[0]

    priority = get_priority(shared)

    return priority

def get_priority(c):
    return ord(c) - 38 if c.isupper() else ord(c) - 96

total = 0

for l in lines:
    p = handle_line(l)

    total += p

print(total)
