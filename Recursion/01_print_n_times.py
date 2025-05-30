def print_hello_left_to_right(n):
    """
    Prints 'Hello' n times using decrease-and-conquer strategy from left to right.
    """

    def helper(n):
        if n == 0:
            return
        print("Hello", end=" ")
        helper(n - 1)

    helper(n)


def print_hello_right_to_left(n):
    """
    Prints 'Hello' n times using decrease-and-conquer strategy from right to left.
    """

    def helper(n):
        if n == 0:
            return
        helper(n - 1)
        print("Hello", end=" ")

    helper(n)


def print_hello_divide_and_conquer(n):
    """
    Prints 'Hello' n times using divide-and-conquer strategy.
    """

    def helper(n):
        if n == 1:
            print("Hello", end=" ")
            return

        half = n // 2
        helper(half)
        helper(n - half)

    helper(n)


if __name__ == "__main__":
    print_hello_left_to_right(5)
    print()

    print_hello_right_to_left(5)
    print()

    print_hello_divide_and_conquer(5)
    print()
