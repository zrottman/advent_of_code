from enum import Enum

LineType = Enum('LineType', ['IN_CD', 'IN_LS', 'OUT_DIR', 'OUT_FILE'])

class MaxHeap:
    def __init__(self):
        self.items = []
        self.length = 0

    def parent_idx(self, child_idx): return (child_idx - 1) // 2
    def left_child_idx(self, parent_idx): return (parent_idx * 2) + 1
    def right_child_idx(self, parent_idx): return (parent_idx * 2) + 2

    def has_parent(self, child_idx): return 0 <= self.parent_idx(child_idx) < self.length
    def has_left_child(self, parent_idx): return 0 <= self.left_child_idx(parent_idx) < self.length
    def has_right_child(self, parent_idx): return 0 <= self.right_child_idx(parent_idx) < self.length

    def get_parent(self, child_idx): return self.items[self.parent_idx(child_idx)]
    def get_left_child(self, parent_idx): return self.items[self.left_child_idx(parent_idx)]
    def get_right_child(self, parent_idx): return self.items[self.right_child_idx(parent_idx)]

    def swap(self, idx_one, idx_two):
        self.items[idx_one], self.items[idx_two] = self.items[idx_two], self.items[idx_one]

    def insert(self, node):
        self.items.append(node)
        idx = self.length
        self.length += 1
        idx = self.heapify_up(idx)
        self.heapify_down(idx)

    def poll(self):
        if self.length == 0:
            return None
        self.length -= 1
        self.swap(0, self.length)
        polled = self.items[self.length]
        self.heapify_down(0)
        return polled

    def heapify_up(self, idx):
        while self.has_parent(idx) and self.items[idx].size > self.get_parent(idx).size:
            self.swap(idx, self.parent_idx(idx))
            idx = self.parent_idx(idx)
        return idx

    def heapify_down(self, idx):
        while ((self.has_left_child(idx) and self.get_left_child(idx).size > self.items[idx].size) or
               (self.has_right_child(idx) and self.get_right_child(idx).size > self.items[idx].size)):
            if self.has_left_child(idx) and self.has_right_child(idx):
                if self.get_left_child(idx).size > self.get_right_child(idx).size:
                    self.swap(idx, self.left_child_idx(idx))
                    idx = self.left_child_idx(idx)
                else:
                    self.swap(idx, self.right_child_idx(idx))
                    idx = self.right_child_idx(idx)
            elif self.has_left_child(idx):
                self.swap(idx, self.left_child_idx(idx))
                idx = self.left_child_idx(idx)
        return idx
        

class Node:

    def __init__(self, name, size=0):
        self.name = name 
        self.size = size
        self.children = []

    def find_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
        return None

    def display(self, indent=0):
        if not self:
            return
        print("{}{}: {} ({} children)".format('   ' * indent, self.name, self.size, len(self.children)))
        for child in self.children:
            child.display(indent + 1)


class Parser:

    def __init__(self):
        self.path = []
        self.data = open("data/day07_data", "r")
        self.root = None
        self.part_one = MaxHeap()
        self.part_two = MaxHeap()

        self.parse() # parse file tree
        self.audit_memory(self.root) # recursively talley memory

    def advance(self):
        return self.data.readline().strip()

    def get_line_type(self, line):
        if line[1] == 'cd':
            return LineType.IN_CD
        elif line[1] == 'ls':
            return LineType.IN_LS
        elif line[0] == 'dir':
            return LineType.OUT_DIR
        else:
            return LineType.OUT_FILE

    def get_cur_dir(self):
        if len(self.path) == 0:
            return None
        return self.path[-1]

    def parse(self):
        while (line := self.advance()):
            line = line.split(' ')
            match self.get_line_type(line):
                case LineType.IN_CD:
                    self.cd(line[2])
                case LineType.IN_LS:
                    pass
                case LineType.OUT_DIR:
                    self.add_dir(line[1])
                case LineType.OUT_FILE:
                    self.add_file(line[1], line[0])
        self.close()

    def cd(self, dn):
        cur_dir = self.get_cur_dir()
        if not cur_dir:  # we're at root
            if dn != '/':
                raise SyntaxError(f"Expected '/', got {dn}")
            self.root = Node(dn)
            self.path.append(self.root)
        elif dn == '..': # move up
            self.path.pop()
            if len(self.path) == 0:
                raise SyntaxError("Length of path cannot be 0")
        else:            # move down
            if not (child := cur_dir.find_child(dn)):
                raise SyntaxError(f"Child `{dn}` not found.")
            self.path.append(child)

    def add_dir(self, dn):
        cur_dir = self.path[-1]
        if not (match := cur_dir.find_child(dn)):
            cur_dir.children.append(Node(dn))

    def add_file(self, fn, fs):
        cur_dir = self.path[-1]
        if not (match := cur_dir.find_child(fn)):
            cur_dir.children.append(Node(fn, int(fs)))

    def close(self):
        self.data.close()

    def audit_memory(self, root):
        if not root:
            return 0
        for child in root.children:
            root.size += self.audit_memory(child)
        if len(root.children) > 0: # a directory
            self.part_two.insert(root)
            if root.size < 100000:
                self.part_one.insert(root)
        return root.size


parser = Parser() 

# PART 1
part_one_total = 0
while (polled := parser.part_one.poll()):
    part_one_total += polled.size
    #print("{}: {}".format(polled.name, polled.size))

print("Part 1: Sum of all directory sizes < 100000")
print(part_one_total)
print()


# PART 2
mem_used = parser.part_two.poll().size
mem_avail = 70000000 - mem_used
mem_needed = 30000000 - mem_avail

while (polled := parser.part_two.poll()) and polled.size > mem_needed:
    candidate = polled

print(f"Part 2: Directory to delete to free 30000000")
print(f"Memory used: {mem_used}")
print(f"Memory available: {mem_avail}")
print(f"Memory needed: {mem_needed}")
print(f"Delete `{candidate.name}` (size {candidate.size})")
