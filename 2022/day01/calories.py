data = []

with open('input', 'r') as f:
    while (line := f.readline()):
        data.append(line.strip())

# Part 1: print total calories of elf carrying most calories
max_cals = 0
cur_cals = 0

for item in data:
    if item == '':
        max_cals = max(max_cals, cur_cals)
        cur_cals = 0
        continue
    cur_cals += int(item)

print(max_cals)

# Part 2: print total calories of top 3 elves with most calories
max_cals = [0, 0, 0]
cur_cals = 0

for item in data:
    if item == '':
        if cur_cals > max_cals[0]:
            max_cals[0] = cur_cals
            max_cals.sort()
        cur_cals = 0
        continue
    cur_cals += int(item)

print(sum(max_cals))
