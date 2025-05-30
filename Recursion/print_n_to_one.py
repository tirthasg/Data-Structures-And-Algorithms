def print_from_n_v1(n):
    if n == 0:
        return

    print(n, end=" ")
    print_from_n_v1(n - 1)


def print_from_n_v2(n):
    def helper(n, curr):
        if curr > n:
            return

        helper(n, curr + 1)
        print(curr, end=" ")

    helper(n, 1)


def print_from_n_v3(n):
    def helper(high, low):
        if high == low:
            print(high, end=" ")
            return

        mid = high + (low - high) // 2

        helper(high, mid + 1)
        helper(mid, low)

    helper(n, 1)


print_from_n_v1(5)
print()

print_from_n_v2(5)
print()

print_from_n_v3(5)
print()
