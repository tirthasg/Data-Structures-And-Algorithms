def permute(nums):
    def helper(nums, index, slate):
        if index == len(nums):
            result.append(slate[:])
            return

        for pick in range(index, len(nums)):
            nums[index], nums[pick] = nums[pick], nums[index]
            slate.append(nums[index])
            helper(nums, index + 1, slate)
            slate.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    print(permute([0, 1]))
    print(permute([1]))
