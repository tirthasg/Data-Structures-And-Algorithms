def permute_unique(nums):
    def helper(nums, index, slate):
        if index == len(nums):
            result.append(slate[:])
            return

        uniques = set()
        for pick in range(index, len(nums)):
            if nums[pick] in uniques:
                continue

            uniques.add(nums[pick])
            nums[index], nums[pick] = nums[pick], nums[index]
            slate.append(nums[index])
            helper(nums, index + 1, slate)
            slate.pop()
            nums[index], nums[pick] = nums[pick], nums[index]

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(permute_unique([1, 1, 2]))
    print(permute_unique([1, 2, 3]))
