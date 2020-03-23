# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    dice.sort() # order list low->high
    total = 0 # initial score

    if category is YACHT:                   # YATCH rule
        if dice.count(dice[0]) == 5: total = 50

    elif category in range(1,7):            # ONES-SIXES rule
        total = len([ x for x in dice if x == category ]) * category

    elif category is FULL_HOUSE:            # FULL HOUSE rule
        if dice[0] == dice[1] & dice[1] != dice[4]:
            if dice[1] == dice[2]:
                if dice[3] == dice[4]:
                    total = sum(dice)
            elif dice[2] == dice[3] and dice[2] == dice[4]:
                total = sum(dice)

    elif category is FOUR_OF_A_KIND:        # FOUR OF A KIND rule
        for x in dice:
            if dice.count(x) == 4 or dice.count(x) == 5: 
                total = x*4

    elif category is LITTLE_STRAIGHT:       # LITTLE STRAIGHT
        if set(dice) == {1,2,3,4,5}:
            total = 30

    elif category is BIG_STRAIGHT:          # BIG STRAIGHT
        if set(dice) == {2,3,4,5,6}:
            total = 30

    elif category is CHOICE:                # CHOICE
        return sum(dice)
    return total