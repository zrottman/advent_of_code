# Part 1 key
key_one = {
        'A': { # rock
            'X': 1 + 3, # play rock (1) for draw (3)
            'Y': 2 + 6, # play paper (2) for win (6)
            'Z': 3 + 0  # play scissors (3) for loss (0)
            },
        'B': { # paper
            'X': 1 + 0,
            'Y': 2 + 3,
            'Z': 3 + 6
            },
        'C': { # scissors
            'X': 1 + 6,
            'Y': 2 + 0,
            'Z': 3 + 3
            }
        }

# Part 2 key
key_two = {
        'A': { # rock
            'X': 3 + 0, # to lose (0) play scissors (3)
            'Y': 1 + 3, # to draw (3) play rock (1)
            'Z': 2 + 6  # to win (6) play paper (2)
            },
        'B': { # paper
            'X': 1 + 0,
            'Y': 2 + 3,
            'Z': 3 + 6
            },
        'C': { # scissors
            'X': 2 + 0,
            'Y': 3 + 3,
            'Z': 1 + 6
            }
        }

score_one = score_two = 0

with open('data/day02_data', 'r') as f:
    while (line := f.readline()):
        you, me = line.split()
        score_one += key_one[you][me]
        score_two += key_two[you][me]

print(f"Part 1 score: {score_one}");
print(f"Part 2 score: {score_two}");
