#!/usr/bin/python3

with open('06_input', 'r') as f:
    lines = f.readlines()

def find_marker(s):
    buf = 14
    for i in range(len(s)-buf):
        if len(set(list(s[i:i+buf]))) == buf:
            return i + buf

for l in lines:
    print(find_marker(l.strip()))
