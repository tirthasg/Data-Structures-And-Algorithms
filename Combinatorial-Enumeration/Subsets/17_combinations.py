def combine(n, k):
    def helper(nums, i, slate):
        if len(slate) == k:
            result.append(slate[:])
            return

        if i == len(nums):
            return

        helper(nums, i + 1, slate)

        slate.append(nums[i])
        helper(nums, i + 1, slate)
        slate.pop()

    result = []
    helper(range(1, n + 1), 0, [])
    return result


def combine_v2(n, k):
    def helper(i, slate):
        if len(slate) == k:
            result.append(slate[:])
            return

        if i == n + 1:
            return

        for pick in range(i, n + 1):
            slate.append(pick)
            helper(pick + 1, slate)
            slate.pop()

    result = []
    helper(1, [])
    return result


if __name__ == "__main__":
    print(combine(n=4, k=2))
    print(combine(n=1, k=1))
    print()
    print(combine_v2(n=4, k=2))
    print(combine_v2(n=1, k=1))
