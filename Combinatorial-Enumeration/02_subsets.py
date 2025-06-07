def subsets(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
            return

        helper(nums, i + 1, slate)

        slate.append(nums[i])
        helper(nums, i + 1, slate)
        slate.pop()

    result = []
    helper(nums, 0, [])
    return result


def lexicographic_subsets(nums):
    def helper(nums, i, slate):
        result.append(slate[:])

        if i == len(nums):
            return

        for pick in range(i, len(nums)):
            slate.append(nums[pick])
            helper(nums, pick + 1, slate)
            slate.pop()

    nums.sort()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(subsets([0]))

    print(lexicographic_subsets([1, 2, 3]))
    print(lexicographic_subsets([0]))
