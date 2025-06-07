def subsets_with_duplicates(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
            return

        count = 0
        for pick in range(i, len(nums)):
            if nums[pick] != nums[i]:
                break
            count += 1

        helper(nums, i + count, slate)

        for _ in range(count):
            slate.append(nums[i])
            helper(nums, i + count, slate)

        for _ in range(count):
            slate.pop()

    nums.sort()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(subsets_with_duplicates([1, 2, 2]))
    print(subsets_with_duplicates([0]))
