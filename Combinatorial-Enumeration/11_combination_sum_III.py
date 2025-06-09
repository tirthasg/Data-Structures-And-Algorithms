def combination_sum_3(k, n):
    def helper(nums, i, slate):
        if len(slate) == k and sum(slate) == n:
            result.append(slate[:])
            return

        if len(slate) > k or sum(slate) > n:
            return

        if i == len(nums):
            return

        helper(nums, i + 1, slate)

        slate.append(nums[i])
        helper(nums, i + 1, slate)
        slate.pop()

    result = []
    helper(list(range(1, 10)), 0, [])
    return result


def combination_sum_3_optimized(k, n):
    def helper(i, slate, slate_sum):
        if len(slate) == k and slate_sum == n:
            result.append(slate[:])
            return

        if len(slate) > k or slate_sum > n:
            return

        if i == 10:
            return

        helper(i + 1, slate, slate_sum)

        slate.append(i)
        helper(i + 1, slate, slate_sum + i)
        slate.pop()

    result = []
    helper(1, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum_3(k=3, n=7))
    print(combination_sum_3(k=3, n=9))
    print(combination_sum_3(k=4, n=1))

    print(combination_sum_3_optimized(k=3, n=7))
    print(combination_sum_3_optimized(k=3, n=9))
    print(combination_sum_3_optimized(k=4, n=1))
