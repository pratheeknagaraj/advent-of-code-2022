#!/usr/bin/python3

with open('09_input', 'r') as f:
    lines = f.readlines()

visited = set()

head = (0,0)
tail = (0,0)

visited.add(tail)

def touching(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    elif a[0] == b[0] and abs(a[1] - b[1]) == 1:
        return True
    elif a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True
    elif abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1:
        return True

    return False

for step in lines:
    direction, count = step.strip().split()
    count = int(count)

    for i in range(count):
        if direction == 'R':
            head = (head[0]+1, head[1])
        elif direction == 'L':
            head = (head[0]-1, head[1])
        elif direction == 'U':
            head = (head[0], head[1]-1)
        elif direction == 'D':
            head = (head[0], head[1]+1)

        if not touching(head, tail):
            # Move

            if head[0] == tail[0]:
                if head[1] > tail[1]:
                    tail = (tail[0], tail[1]+1)
                else:
                    tail = (tail[0], tail[1]-1)
            elif head[1] == tail[1]:
                if head[0] > tail[0]:
                    tail = (tail[0]+1, tail[1])
                else:
                    tail = (tail[0]-1, tail[1])
            else:
                if direction == 'R':
                    tail = (tail[0]+1, head[1])
                elif direction == 'L':
                    tail = (tail[0]-1, head[1])
                elif direction == 'U':
                    tail = (head[0], tail[1]-1)
                elif direction == 'D':
                    tail = (head[0], tail[1]+1)

            if tail not in visited:
                visited.add(tail)

print(len(visited))
