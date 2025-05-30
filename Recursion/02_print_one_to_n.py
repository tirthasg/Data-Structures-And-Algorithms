def print_till_n_v1(n):
    # Using Decrease-and-conquer strategy from right
    def helper(n):
        if n == 0:
            return

        helper(n - 1)
        print(n, end=" ")

    helper(n)


def print_till_n_v2(n):
    # Using Decrease-and-conquer strategy from left
    def helper(n, curr):
        if curr > n:
            return

        print(curr, end=" ")
        helper(n, curr + 1)

    helper(n, 1)


def print_till_n_v3(n):
    # Using Divide-and-conquer strategy
    def helper(low, high):
        if low > high:
            return

        if low == high:
            print(low, end=" ")
            return

        mid = low + (high - low) // 2
        helper(low, mid)
        helper(mid + 1, high)

    helper(1, n)


print_till_n_v1(5)
print()

print_till_n_v2(5)
print()

print_till_n_v3(5)
print()
