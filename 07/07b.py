#!/usr/bin/python3

with open('07_input', 'r') as f:
    lines = f.readlines()

class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.dirs = {}
        self.files = {}
        self.size = None

        self.parent = parent

    def __repr__(self):
        return self.__str__

    def __str__(self):
        data = {
            'name': self.name,
            'dirs': self.dirs.keys(),
            'files': self.files.items(),
            'size': self.size,
            'parent': self.parent.name if self.parent else 'None'
        }

        return str(data)

root = Directory('/')

cwd = root

listing = False

for line in lines:
    l = line.strip()
    if l.startswith('$'):
        # Command
        parts = l.split()
        cmd = parts[1]
        if cmd == 'cd':
            target = parts[2]
            listing == False
            if target == '/':
                cwd = root
            elif target == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.dirs[target]
        elif cmd == 'ls':
            listing = True
    else:
        # Output
        if listing == True:
            val, name = l.split()
            if val == 'dir':
                if name not in cwd.dirs:
                    cwd.dirs[name] = Directory(name, cwd)
            else:
                if name not in cwd.files:
                    cwd.files[name] = int(val)


def compute_size(node):
    dir_size = 0
    if node.dirs.keys():
        for d in node.dirs.values():
            dir_size += compute_size(d)

    dir_size += sum(node.files.values())
    node.size = dir_size

    return dir_size

compute_size(root)


disk_size = 70000000
req_size = 30000000

unused = disk_size - root.size
min_del_size = req_size - unused

queue = [root]

min_found = disk_size

while queue:
    cur = queue.pop(0)
    queue.extend(cur.dirs.values())

    if cur.size >= min_del_size and cur.size <= min_found:
        min_found = cur.size

print(min_found)
