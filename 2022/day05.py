stacks_one = [[] for _ in range(9)]
line_num = 0

with open("data/day05_data", "r") as f:
    while (line := f.readline()):
        
        # first 8 rows: ingest initial stack state from top to bottom
        if line_num < 8:
            for i in range(9):
                col = 1 + (i*4)
                if col >= len(line):
                    break
                elif line[col] == ' ':
                    continue
                stacks_one[i].append(line[col])

        # 9th row: reverse stack state and make deep copy to handle parts 1 & 2
        elif line_num == 8:
            for stack in stacks_one:
                stack.reverse()
            stacks_two = [stack.copy() for stack in stacks_one]

        # remaining rows: apply moves to stacks_one and stacks_two
        elif line_num > 9:
            instr = line.split()
            repeat = int(instr[1])
            from_col = int(instr[3]) - 1
            to_col  = int(instr[5]) - 1
            
            # Part 1
            for _ in range(repeat):
                stacks_one[to_col].append(stacks_one[from_col].pop())

            # Part 2
            tmp = []
            for _ in range(repeat):
                tmp.append(stacks_two[from_col].pop())
            while len(tmp) > 0:
                stacks_two[to_col].append(tmp.pop())

        line_num += 1


# Part 1 output
print("Part 1: ", end="")
for stack in stacks_one:
    print(f"{stack[-1]}", end="")
print()
for i, stack in enumerate(stacks_one):
    print(f"{i+1}: ", end="")
    for item in stack:
        print(f"[{item}]", end=" ")
    print()
print()

# Part 2 output
print("Part 2: ", end="")
for stack in stacks_two:
    print(f"{stack[-1]}", end="")
print()
for i, stack in enumerate(stacks_two):
    print(f"{i+1}: ", end="")
    for item in stack:
        print(f"[{item}]", end=" ")
    print()
print()
