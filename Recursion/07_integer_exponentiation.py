def power_left_to_right(base, exponent):
    """
    Computes base^exponent using a decrease-and-conquer strategy (left to right).
    """

    def helper(base, exponent, curr):
        if curr > exponent:
            return 1

        return base * helper(base, exponent, curr + 1)

    return helper(base, exponent, 1)


def power_right_to_left(base, exponent):
    """
    Computes base^exponent using a decrease-and-conquer strategy (right to left).
    """

    def helper(base, exponent):
        if exponent == 0:
            return 1

        return base * helper(base, exponent - 1)

    return helper(base, exponent)


def power_divide_and_conquer(base, exponent):
    """
    Computes base^exponent using divide-and-conquer strategy.
    """

    def helper(base, low, high):
        if low == high:
            return base

        mid = (low + high) // 2
        return helper(base, low, mid) * helper(base, mid + 1, high)

    return helper(base, 1, exponent)


def power_better_divide_and_conquer(base, exponent):
    """
    Computes base^exponent using exponentiation by squaring.
    """

    def helper(base, exponent):
        if exponent == 0:
            return 1

        half = helper(base, exponent // 2)
        result = half * half
        if exponent % 2 == 0:
            return result

        return base * result

    return helper(base, exponent)


if __name__ == "__main__":
    print(power_right_to_left(2, 5))
    print(power_left_to_right(2, 5))
    print(power_divide_and_conquer(2, 5))
    print(power_better_divide_and_conquer(2, 5))
