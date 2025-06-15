def find_subsequences_v1(nums):
    def helper(nums, i, slate):
        if len(slate) > 1 and slate[-2] > slate[-1]:
            return

        if len(slate) > 1:
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


def find_subsequences_v2(nums):
    def helper(nums, i, slate):
        if len(slate) > 1:
            result.append(slate[:])

        if i == len(nums):
            return

        uniques = set()
        for pick in range(i, len(nums)):
            if nums[pick] in uniques:
                continue
            uniques.add(nums[pick])

            if len(slate) == 0 or slate[-1] <= nums[pick]:
                slate.append(nums[pick])
                helper(nums, pick + 1, slate)
                slate.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(find_subsequences_v1([4, 6, 7, 7]))
    print(find_subsequences_v1([4, 4, 3, 2, 1]))
    print()
    print(find_subsequences_v2([4, 6, 7, 7]))
    print(find_subsequences_v2([4, 4, 3, 2, 1]))
