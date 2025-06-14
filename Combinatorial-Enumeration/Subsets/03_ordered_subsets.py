def ordered_subsets(nums):
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
    print(ordered_subsets([1, 2, 3]))
    print(ordered_subsets([3, 1, 2]))
