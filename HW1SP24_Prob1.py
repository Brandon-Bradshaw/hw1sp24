from Die import rollFairDie as rfd

def main(N=1000):
    """
    Prints probablities of rolling each possible number out of 1000 rolls.
    :return: None
    :param N: How many times I want to roll
    """
    ones=0
    twos=0
    threes=0
    fours=0
    fives=0
    sixes=0

    for i in range(0,N):
        y = rfd()
        if y==1:
            ones+=1
        if y==2:
            twos+=1
        if y==3:
            threes+=1
        if y==4:
            fours+=1
        if y==5:
            fives+=1
        if y==6:
            sixes+=1
    #print(y)
    print("After rolling the die {:0d} times:".format(N))
    print("probabilty of rolling a 1: {Ones:0.4f}".format(Ones=ones/N))
    print("probabilty of rolling a 2: {Twos:0.4f}".format(Twos=twos/N))
    print("probabilty of rolling a 3: {Threes:0.4f}".format(Threes=threes/N))
    print("probabilty of rolling a 4: {Fours:0.4f}".format(Fours=fours/N))
    print("probabilty of rolling a 5: {Fives:0.4f}".format(Fives=fives/N))
    print("probabilty of rolling a 6: {Sixes:0.4f}".format(Sixes=sixes/N))

main(1000)

def main2(N=10000):
    """
    Prints probablities of rolling each possible number out of 10000 rolls.
    :return: None
    :param N: How many times I want to roll
    """
    ones=0
    twos=0
    threes=0
    fours=0
    fives=0
    sixes=0

    for i in range(0,N):
        y = rfd()
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
    # print(y)
    print("After rolling the die {:0d} times:".format(N))
    print("probabilty of rolling a 1: {Ones:0.4f}".format(Ones=ones / N))
    print("probabilty of rolling a 2: {Twos:0.4f}".format(Twos=twos / N))
    print("probabilty of rolling a 3: {Threes:0.4f}".format(Threes=threes / N))
    print("probabilty of rolling a 4: {Fours:0.4f}".format(Fours=fours / N))
    print("probabilty of rolling a 5: {Fives:0.4f}".format(Fives=fives / N))
    print("probabilty of rolling a 6: {Sixes:0.4f}".format(Sixes=sixes / N))

main2(10000)