def print_n_to_1_left_to_right(n):
    """
    Prints numbers from n to 1 using a decrease-and-conquer strategy (left to right).
    """

    def helper(n):
        if n == 0:
            return

        print(n, end=" ")
        helper(n - 1)

    helper(n)


def print_n_to_1_right_to_left(n):
    """
    Prints numbers from n to 1 using a decrease-and-conquer strategy (right to left).
    """

    def helper(n, curr):
        if curr > n:
            return

        helper(n, curr + 1)
        print(curr, end=" ")

    helper(n, 1)


def print_n_to_1_divide_and_conquer(n):
    """
    Prints numbers from n to 1 using a divide-and-conquer strategy.
    """

    def helper(high, low):
        if high == low:
            print(high, end=" ")
            return

        mid = (high + low) // 2
        helper(high, mid + 1)
        helper(mid, low)

    helper(n, 1)


if __name__ == "__main__":
    print_n_to_1_left_to_right(5)
    print()

    print_n_to_1_right_to_left(5)
    print()

    print_n_to_1_divide_and_conquer(5)
    print()
