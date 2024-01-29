from Die import rollFairDie as rfd, rollUnFairDie
def rollDice(N=3, fair=True):
    """
    Rolls N number of fair or unfair dice
    :param N(int): Number of Dice rolled
    :param fair: True for Fair Die, False for UnFair die
    :return: int - Total Score
    """
    if fair:
        scores = [rfd() for _ in range(N)]
    else:
        scores = [rollUnFairDie() for _ in range(N)]
    return sum(scores)
if __name__ == "__main__":
    total_score_fair = rollDice(N=3, fair=True)
    print("Total score with fair dice:", total_score_fair)
    total_score_unfair = rollDice(N=3, fair=False)
    print("Total score with unfair dice:", total_score_unfair)