file = open('data.txt')

lines = file.readlines()

move_map = {
    "A": {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
    },
    "B": {
        "BX": 0,
        "BY": 3,
        "BZ": 6,
    },
    "C": {
        "CX": 6,
        "CY": 0,
        "CZ": 3,
    }
}

move_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# Part 1
# A for Rock
# B for Paper
# C for Scissors
# X for Rock
# Y for Paper
# Z for Scissors

def checker_1(player_1, player_2):
    return move_map.get(player_1).get(f"{player_1}{player_2}") + move_score.get(f"{player_2}")

print(sum([checker_1(line.split()[0], line.split()[1]) for line in lines]))


# Part 2
# X means you need to lose,
# Y means you need to end the round in a draw,
# Z means you need to win.


def checker_2(player_1, player_2):
    score_map = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    for move, score in move_map.get(player_1).items():
        if score_map.get(player_2) != score:
            continue
        return score + move_score.get(move[1])

print(sum([checker_2(line.split()[0], line.split()[1]) for line in lines]))
