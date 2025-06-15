def combination_sum3(k, n):
    def helper(nums, i, slate, slate_sum):
        if len(slate) > k:
            return

        if slate_sum > n:
            return

        if len(slate) == k and slate_sum == n:
            result.append(slate[:])
            return

        if i == 9:
            return

        helper(nums, i + 1, slate, slate_sum)

        slate.append(nums[i])
        helper(nums, i + 1, slate, slate_sum + nums[i])
        slate.pop()

    result = []
    helper(range(1, 10), 0, [], 0)
    return result


def combination_sum3_v2(k, n):
    def helper(i, slate, slate_sum):
        if len(slate) > k:
            return

        if slate_sum > n:
            return

        if len(slate) == k and slate_sum == n:
            result.append(slate[:])
            return

        if i == 10:
            return

        for pick in range(i, 10):
            slate.append(pick)
            helper(pick + 1, slate, slate_sum + pick)
            slate.pop()

    result = []
    helper(1, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum3(k=3, n=7))
    print(combination_sum3(k=3, n=9))
    print()
    print(combination_sum3_v2(k=3, n=7))
    print(combination_sum3_v2(k=3, n=9))
