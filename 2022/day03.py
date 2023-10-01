alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
items = {c:i+1 for i, c in enumerate(list(alpha))}

# PART 1
score = 0

with open('data/day03_data', 'r') as f:
    while (line := f.readline().strip()):
        left = set()
        length = len(line)
        common = ''
        for i, char in enumerate(line):
            if i < length // 2:
                left.add(char)
            else:
                if char in left:
                    common = char
                    break
        score += items[common]

print("Part 1: {}".format(score))


# PART 2
score = 0
trio = [None] * 3
count = 0
        
with open('data/day03_data', 'r') as f:
    while (line := f.readline().strip()):
        trio[count % 3] = set()
        for char in line:
            trio[count % 3].add(char)
        count += 1
        if count % 3 == 0:
            common = list(trio[0].intersection(trio[1]).intersection(trio[2]))[0]
            score += items[common]

print("Part 2: {}".format(score))
