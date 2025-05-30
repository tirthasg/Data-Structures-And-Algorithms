def fibonacci_v1(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_v1(n - 1) + fibonacci_v1(n - 2)


def fibonacci_v2(n):
    def helper(n, first, second):
        if n == 0:
            return first

        if n == 1:
            return second

        return helper(n - 1, second, first + second)

    return helper(n, 0, 1)


print(fibonacci_v1(6))
print(fibonacci_v2(6))
