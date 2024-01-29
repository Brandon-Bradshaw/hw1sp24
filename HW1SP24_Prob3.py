import random
def generate_normal_distribution(mean, std_dev, size):
    """
    Produces an array of size N around a normally distributed population
    :param mean: Mean of normal distribution
    :param std_dev: Standard Deviation of normal distribution
    :param size: Size of the array
    :return: Array of size N
    """
    return [random.normalvariate(mean, std_dev) for _ in range(size)]

def calculate_sample_statistics(data):
    """
    Prints the Mean and Standard Deviation of the data
    :param data: List of data points
    :return: Mean and Standard Deviation of the data
    """
    n = len(data)
    mean = sum(data) / n
    std_dev = (sum((x - mean) ** 2 for x in data) / n) ** 0.5
    return mean, std_dev

def main():
    mean = 10.0
    std_dev = 2.0
    data = generate_normal_distribution(mean, std_dev, size=1000)
    sample_mean, sample_std_dev = calculate_sample_statistics(data)
    print("Sample Mean:", sample_mean)
    print("Sample Standard Deviation:", sample_std_dev)

if __name__ == "__main__":
    main()