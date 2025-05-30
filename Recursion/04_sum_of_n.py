def sum_1_to_n_left_to_right(n):
    """
    Returns the sum of numbers from 1 to n using a decrease-and-conquer strategy (left to right).
    """

    def helper(n, curr):
        if curr > n:
            return 0

        return curr + helper(n, curr + 1)

    return helper(n, 1)


def sum_1_to_n_right_to_left(n):
    """
    Returns the sum of numbers from 1 to n using a decrease-and-conquer strategy (right to left).
    """

    def helper(n):
        if n == 0:
            return 0

        return helper(n - 1) + n

    return helper(n)


def sum_1_to_n_divide_and_conquer(n):
    """
    Returns the sum of numbers from 1 to n using a divide-and-conquer strategy.
    """

    def helper(start, end):
        if start == end:
            return start

        mid = (start + end) // 2
        return helper(start, mid) + helper(mid + 1, end)

    return helper(1, n)


if __name__ == "__main__":
    print(sum_1_to_n_right_to_left(5))
    print(sum_1_to_n_left_to_right(5))
    print(sum_1_to_n_divide_and_conquer(5))
