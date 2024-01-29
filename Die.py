import random
def rollFairDie():
    """
    This function takes no arguments
    :return: an integer between 1 and 6 inclusively, but random. Meaning each roll is independent and does not rely on past or future rolls.
    """
    x=random.random()
    if (x <= 1.0 / 6):
        return 1
    elif (x <= 2.0 / 6):
        return 2
    elif (x <= 3.0 / 6):
        return 3
    elif (x <= 4.0 / 6):
        return 4
    elif (x <= 5.0 / 6):
        return 5
    elif (x <= 6.0 / 6):
        return 6
    print(x)

ones=0

for i in range(0,1000):
    y = rollFairDie()
    if y==1:
        ones+=1
    #print(y)
print(ones)

import random
def rollUnFairDie():
    """
    This function takes no arguments
    :return: An integer between 1 and 6, with 1 having a probability of 0.2
    """
    x=random.random()
    if (0.0 <= x < 0.2):
        return 1
    elif (0.2 <= x < 1.0 / 6 + 0.2):
        return 2
    elif (1.0 / 6 + 0.2 <= x < 2.0 / 6 + 0.2):
        return 3
    elif (2.0 / 6 + 0.2 <= x < 3.0 / 6 + 0.2):
        return 4
    elif (3.0 / 6 + 0.2 <= x < 4.0 / 6 + 0.2):
        return 5
    else:
        return 6
    print(x)
ones=0

for i in range(0,1000):
    y = rollUnFairDie()
    if y==1:
        ones+=1
    #print(y)
print(ones)

import random

def main3():
    """
    Prints the probability of each number after the die has been rolled 10000 times
    :return: Nothing
    """
    num_rolls = 10000
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for _ in range(num_rolls):
        y = rollUnFairDie()
        if y == 1:
            ones += 1
        if y == 2:
            twos += 1
        if y == 3:
            threes += 1
        if y == 4:
            fours += 1
        if y == 5:
            fives += 1
        if y == 6:
            sixes += 1
        result = rollUnFairDie()
    print("After rolling the die 10,000 times:")
    print (f"Probability of rolling a 1: {ones / 10000: .4f}")
    print (f"Probability of rolling a 2: {twos / 10000: .4f}")
    print (f"Probability of rolling a 3: {threes / 10000: .4f}")
    print (f"Probability of rolling a 4: {fours / 10000: .4f}")
    print (f"Probability of rolling a 5: {fives / 10000: .4f}")
    print (f"Probability of rolling a 6: {sixes / 10000: .4f}")

if __name__ == "__main__":
    main3()
