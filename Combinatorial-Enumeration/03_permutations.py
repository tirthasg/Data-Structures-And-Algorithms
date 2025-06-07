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


def permute_without_slate(nums):
    def helper(nums, i):
        if i == len(nums):
            result.append(nums[:])
            return

        for pick in range(i, len(nums)):
            nums[i], nums[pick] = nums[pick], nums[i]
            helper(nums, i + 1)
            nums[i], nums[pick] = nums[pick], nums[i]

    result = []
    helper(nums, 0)
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    print(permute([0, 1]))
    print(permute([1]))

    print(permute_without_slate([1, 2, 3]))
    print(permute_without_slate([0, 1]))
    print(permute_without_slate([1]))
