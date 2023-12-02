#!/usr/bin/python3

from numpy import lcm

with open('11_input', 'r') as f:
    lines = f.readlines()

monkey_count = len(lines)//7 + 1

monkeys = []

lcm_test = None

def send(new_val, monkey_num):
    monkeys[monkey_num].items.append(new_val)

class Monkey:

    def __init__(self, num):
        self.num = num
        self.items = []
        self.inspected = 0

    def setup(self, lines):
        self.items = [int(i) for i in lines[1].split(':')[1].split(',')]
        self.operation_parts = lines[2].split('=')[1].strip()
        self.test_num = int(lines[3].strip().split()[-1])
        self.if_true = int(lines[4].strip().split()[-1])
        self.if_false = int(lines[5].strip().split()[-1])

    def run(self):
        while self.items:
            i = self.items.pop(0)
            self.inspect(i)
            self.inspected += 1

    def inspect(self, i):
        eval_str = self.operation_parts.replace('old', str(i))
        val = eval(eval_str)
        new_val = val % lcm_test

        if new_val % self.test_num == 0:
            send(new_val, self.if_true)
        else:
            send(new_val, self.if_false)

    def __str__(self):
        return str((self.num, self.items, self.inspected))

    def __repr__(self):
        return self.__str__

for i in range(monkey_count):
    m = Monkey(i)
    m.setup(lines[i*7:i*7+6])
    monkeys.append(m)

lcm_test = lcm.reduce([m.test_num for m in monkeys])

round_count = 10000

def run_round():
    for m in monkeys:
        m.run()

for i in range(round_count):
    run_round()

inspection_totals = sorted([m.inspected for m in monkeys], reverse=True)

monkey_business = inspection_totals[0] * inspection_totals[1]
print(monkey_business)
