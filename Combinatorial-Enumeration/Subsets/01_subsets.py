def subsets(nums):
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


def subsets_include_first(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
            return

        slate.append(nums[i])
        helper(nums, i + 1, slate)
        slate.pop()

        helper(nums, i + 1, slate)

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(subsets([0]))
    print(subsets([]))

    print(subsets_include_first([1, 2, 3]))
    print(subsets_include_first([0]))
    print(subsets_include_first([]))
