from Dice import rollDice
def main():
    """
    Prints probability for each possible score
    :return: None
    """
    #Number of Dice
    n = 3
    #Number of rolls
    num_rolls = 1000
    scores_count = {score: 0 for score in range(n, 6 * n +1)}
    for _ in range(num_rolls):
        total_score = rollDice(N=n)
        scores_count[total_score] += 1
    print(f"Probability of rolling each possible score with {n} dice:")
    for score, count in scores_count.items():
        probability = count / num_rolls
        print (f"Score {score}: {probability:.3f}")

if __name__ == "__main__":
    main()