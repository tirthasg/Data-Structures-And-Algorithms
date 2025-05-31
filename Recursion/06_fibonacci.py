def fibonacci_recursive(n):
    """
    Computes the nth Fibonacci number using naive recursion.
    Time complexity: O(2^n)
    """

    def helper(n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        return helper(n - 1) + helper(n - 2)

    return helper(n)


def fibonacci_tail_recursive(n):
    """
    Computes the nth Fibonacci number using tail recursion.
    Time complexity: O(n)
    """

    def helper(n, first, second):
        if n == 0:
            return first

        if n == 1:
            return second

        return helper(n - 1, second, first + second)

    return helper(n, 0, 1)


if __name__ == "__main__":
    print(fibonacci_recursive(6))
    print(fibonacci_tail_recursive(6))
