full_overlap = 0
partial_overlap = 0

with open("data/day04_data", "r") as f:
    while (line := f.readline().strip()):
        one, two = line.split(',')
        one_low, one_high = one.split('-')
        two_low, two_high = two.split('-')

        # Part 1: Full overlaps
        if ((int(one_low) <= int(two_low) and int(two_high) <= int(one_high)) or
            (int(two_low) <= int(one_low) and int(one_high) <= int(two_high))):
            full_overlap += 1

        # Part 2: Partial overlaps
        if ((int(one_low) <= int(two_low) and int(two_low) <= int(one_high)) or
            (int(one_low) <= int(two_high) and int(two_high) <= int(one_high)) or
            (int(two_low) <= int(one_low) and int(one_low) <= int(two_high)) or
            (int(two_low) <= int(one_high) and int(one_high) <= int(two_high))):
            partial_overlap += 1

print(f"Full Overlaps   : {full_overlap}")    # Part 1
print(f"Partial Overlaps: {partial_overlap}") # Part 2
