def permute(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
            return

        for pick in range(i, len(nums)):
            nums[i], nums[pick] = nums[pick], nums[i]
            slate.append(nums[i])
            helper(nums, i + 1, slate)
            slate.pop()
            nums[i], nums[pick] = nums[pick], nums[i]

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    print(permute([0, 1]))
    print(permute([1]))
