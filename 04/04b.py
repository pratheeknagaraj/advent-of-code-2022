#!/usr/bin/python3

with open('04_input', 'r') as f:
    lines = f.readlines()

def is_contained(l):
    a, b = l.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

    if a1 <= b1 and b1 <= a2:
        return True
    if a1 <= b2 and b2 <= a2:
        return True
    if a1 <= b1 and b2 <= a2:
        return True
    if b1 <= a1 and a2 <= b2:
        return True

    return False

count = 0
for l in lines:
    if is_contained(l.strip()):
        count += 1

print(count)

