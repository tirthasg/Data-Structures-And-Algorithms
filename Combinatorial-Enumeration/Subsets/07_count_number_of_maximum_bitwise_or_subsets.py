from functools import reduce


def count_max_or_subsets_v1(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            return int(reduce(lambda x, y: x | y, slate, 0) == target)

        total = helper(nums, i + 1, slate)

        slate.append(nums[i])
        total += helper(nums, i + 1, slate)
        slate.pop()

        return total

    target = reduce(lambda x, y: x | y, nums, 0)
    return helper(nums, 0, [])


def count_max_or_subsets_v2(nums):
    def helper(nums, i, or_total):
        if i == len(nums):
            return int(or_total == target)

        return helper(nums, i + 1, or_total) + helper(nums, i + 1, or_total | nums[i])

    target = reduce(lambda x, y: x | y, nums, 0)
    return helper(nums, 0, 0)


if __name__ == "__main__":
    print(count_max_or_subsets_v1([3, 1]))
    print(count_max_or_subsets_v1([2, 2, 2]))
    print(count_max_or_subsets_v1([3, 2, 1, 5]))
    print()
    print(count_max_or_subsets_v2([3, 1]))
    print(count_max_or_subsets_v2([2, 2, 2]))
    print(count_max_or_subsets_v2([3, 2, 1, 5]))
