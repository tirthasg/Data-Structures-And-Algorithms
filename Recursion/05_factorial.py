def factorial_left_to_right(n):
    """
    Computes factorial of n using a decrease-and-conquer strategy (left to right).
    """

    def helper(n, curr):
        if curr > n:
            return 1

        return curr * helper(n, curr + 1)

    return helper(n, 1)


def factorial_right_to_left(n):
    """
    Computes factorial of n using a decrease-and-conquer strategy (right to left).
    """

    def helper(n):
        if n == 0:
            return 1

        return n * helper(n - 1)

    return helper(n)


def factorial_divide_and_conquer(n):
    """
    Computes factorial of n using a divide-and-conquer strategy.
    """

    def helper(low, high):
        if low == high:
            return low

        mid = (low + high) // 2
        return helper(low, mid) * helper(mid + 1, high)

    return helper(1, n)


if __name__ == "__main__":
    print(factorial_right_to_left(5))
    print(factorial_left_to_right(5))
    print(factorial_divide_and_conquer(5))
