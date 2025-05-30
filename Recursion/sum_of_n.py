def sum_till_n_v1(n):
    if n == 0:
        return 0

    return sum_till_n_v1(n - 1) + n


def sum_till_n_v2(n):
    def helper(n, curr):
        if curr > n:
            return 0

        return curr + helper(n, curr + 1)

    return helper(n, 1)


def sum_till_n_v3(n):
    def helper(start, end):
        if start == end:
            return start

        mid = start + (end - start) // 2
        return helper(start, mid) + helper(mid + 1, end)

    return helper(1, n)


print(sum_till_n_v1(5))
print(sum_till_n_v2(5))
print(sum_till_n_v3(5))
