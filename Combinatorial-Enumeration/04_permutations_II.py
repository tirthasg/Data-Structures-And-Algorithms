def permute_unique(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
            return

        uniques = set()
        for pick in range(i, len(nums)):
            if nums[pick] in uniques:
                continue
            uniques.add(nums[i])

            nums[i], nums[pick] = nums[pick], nums[i]
            slate.append(nums[i])
            helper(nums, i + 1, slate)
            slate.pop()
            nums[i], nums[pick] = nums[pick], nums[i]

    result = []
    helper(nums, 0, [])
    return result


def permute_unique_without_slate(nums):
    def helper(nums, i):
        if i == len(nums):
            result.append(nums[:])
            return

        uniques = set()
        for pick in range(i, len(nums)):
            if nums[pick] in uniques:
                continue
            uniques.add(nums[pick])

            nums[i], nums[pick] = nums[pick], nums[i]
            helper(nums, i + 1)
            nums[i], nums[pick] = nums[pick], nums[i]

    result = []
    helper(nums, 0)
    return result


if __name__ == "__main__":
    print(permute_unique([1, 1, 2]))
    print(permute_unique([1, 2, 3]))

    print(permute_unique_without_slate([1, 1, 2]))
    print(permute_unique_without_slate([1, 2, 3]))
