chars_1 = {}
chars_2 = {}
buf_1 = []
buf_2 = []
i = 0
part_1 = None
part_2 = None
with open("data/day06_data", "r") as f:
    while (c := f.read(1)):

        i += 1

        chars_1[c] = chars_1.get(c, 0) + 1
        buf_1.append(c)

        chars_2[c] = chars_2.get(c, 0) + 1
        buf_2.append(c)

        if not part_1 and len(buf_1) > 4:
            remove = buf_1.pop(0)
            chars_1[remove] -= 1
            if chars_1[remove] == 0:
                del chars_1[remove]
            if len(chars_1) == 4:
                part_1 = i

        if not part_2 and len(buf_2) > 14:
            remove = buf_2.pop(0)
            chars_2[remove] -= 1
            if chars_2[remove] == 0:
                del chars_2[remove]
            if len(chars_2) == 14:
                part_2 = i

        if part_1 and part_2:
            break

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

        



