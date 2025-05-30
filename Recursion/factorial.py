def factorial_v1(n):
    def helper(n):
        if n == 0:
            return 1

        return helper(n - 1) * n

    return helper(n)


def factorial_v2(n):
    def helper(n, curr):
        if curr > n:
            return 1

        return curr * helper(n, curr + 1)

    return helper(n, 1)


def factorial_v3(n):
    def helper(low, high):
        if low == high:
            return low

        mid = low + (high - low) // 2
        return helper(low, mid) * helper(mid + 1, high)

    return helper(1, n)


print(factorial_v1(5))
print(factorial_v2(5))
print(factorial_v3(5))
