def permute(n):
    def helper(nums, i, slate):
        if len(slate) > 1:
            if (slate[-2] & 1) == (slate[-1] & 1):
                return

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
    helper(list(range(1, n + 1)), 0, [])
    return result


if __name__ == "__main__":
    print(permute(4))
    print(permute(2))
    print(permute(3))
