def subsequences(nums):
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


if __name__ == "__main__":
    print(subsequences([1, 2, 3]))
