#!/usr/bin/python3

with open('09_input', 'r') as f:
    lines = f.readlines()

visited = set()

class Knot:

    def __init__(self):
        self.x = 0
        self.y = 0

    def pos(self):
        return (self.x, self.y)

    def __str__(self):
        return str(self.pos())

    def __repr__(self):
        return self.__str__()

length = 10
rope = [Knot() for i in range(length)]

visited.add(rope[-1].pos())

def touching(a, b):
    if a.x == b.x and a.y == b.y:
        return True
    elif a.x == b.x and abs(a.y - b.y) == 1:
        return True
    elif a.y == b.y and abs(a.x - b.x) == 1:
        return True
    elif abs(a.x - b.x) == 1 and abs(a.y - b.y) == 1:
        return True

    return False

for step in lines:
    direction, count = step.strip().split()
    count = int(count)

    head = rope[0]

    for i in range(count):
        if direction == 'R':
            head.x, head.y = head.x+1, head.y
        elif direction == 'L':
            head.x, head.y = head.x-1, head.y
        elif direction == 'U':
            head.x, head.y = head.x, head.y-1
        elif direction == 'D':
            head.x, head.y = head.x, head.y+1

        prev = head

        for num, knot in enumerate(rope[1:]):

            if not touching(prev, knot):
                # Move
                if prev.x == knot.x:
                    if prev.y > knot.y:
                        knot.x, knot.y = knot.x, knot.y+1
                    else:
                        knot.x, knot.y = knot.x, knot.y-1
                elif prev.y == knot.y:
                    if prev.x > knot.x:
                        knot.x, knot.y = knot.x+1, knot.y
                    else:
                        knot.x, knot.y = knot.x-1, knot.y
                else:
                    if prev.x - knot.x == 2:
                        knot.x += 1
                        if prev.y > knot.y:
                            knot.y += 1
                        else:
                            knot.y -= 1
                    elif prev.x - knot.x == -2:
                        knot.x -= 1
                        if prev.y > knot.y:
                            knot.y += 1
                        else:
                            knot.y -= 1
                    elif prev.y - knot.y == 2:
                        knot.y += 1
                        if prev.x > knot.x:
                            knot.x += 1
                        else:
                            knot.x -= 1
                    elif prev.y - knot.y == -2:
                        knot.y -= 1
                        if prev.x > knot.x:
                            knot.x += 1
                        else:
                            knot.x -= 1

            prev = knot

        if rope[-1].pos() not in visited:
            visited.add(rope[-1].pos())


print(len(visited))
