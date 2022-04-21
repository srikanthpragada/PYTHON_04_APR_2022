MIN = 0


def iseven(n):
    """
    Checks whether the given number is even.
    :param n: number to check
    :return: True on even, False otherwise
    """
    return n % 2 == 0


def isprime(n):

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':  # running it as script
    print(iseven(10), isprime(10))
