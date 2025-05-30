def print_1_to_n_left_to_right(n):
    """
    Prints numbers from 1 to n using a decrease-and-conquer strategy (left-to-right).
    """

    def helper(n, curr):
        if curr > n:
            return

        print(curr, end=" ")
        helper(n, curr + 1)

    helper(n, 1)


def print_1_to_n_right_to_left(n):
    """
    Prints numbers from 1 to n using a decrease-and-conquer strategy (right-to-left).
    """

    def helper(n):
        if n == 0:
            return

        helper(n - 1)
        print(n, end=" ")

    helper(n)


def print_1_to_n_divide_and_conquer(n):
    """
    Prints numbers from 1 to n using a divide-and-conquer strategy.
    """

    def helper(low, high):
        if low == high:
            print(low, end=" ")
            return

        mid = (low + high) // 2
        helper(low, mid)
        helper(mid + 1, high)

    helper(1, n)


if __name__ == "__main__":
    print_1_to_n_right_to_left(5)
    print()

    print_1_to_n_left_to_right(5)
    print()

    print_1_to_n_divide_and_conquer(5)
    print()
