def subsequences_with_duplicates(nums):
    def helper(nums, i, slate):
        result.append(slate[:])

        if i == len(nums):
            return

        uniques = set()
        for pick in range(i, len(nums)):
            if nums[pick] in uniques:
                continue
            uniques.add(nums[pick])

            slate.append(nums[pick])
            helper(nums, pick + 1, slate)
            slate.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(subsequences_with_duplicates([1, 2, 3]))
    print(subsequences_with_duplicates([1, 2, 2]))
