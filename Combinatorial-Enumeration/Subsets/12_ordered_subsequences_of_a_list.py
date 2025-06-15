def ordered_subsequences(nums):
    def helper(nums, i, slate):
        result.append(slate[:])

        if i == len(nums):
            return

        for pick in range(i, len(nums)):
            slate.append(nums[pick])
            helper(nums, pick + 1, slate)
            slate.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(ordered_subsequences([1, 2, 3]))
