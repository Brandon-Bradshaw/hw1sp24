import random
def rollFairDie():
    """
    This function takes no arguments and returns
    :return: an integer between 1 and 6 inclusively, but random. Meaning each roll is independent and doesnt rely on past or future rolls.
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
for i in range(0,1000000):
    y = rollFairDie()
    if y==1:
        ones+=1
    #print(y)
print(ones)
