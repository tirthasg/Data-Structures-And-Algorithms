def subsets(nums):
    def helper(nums, index, slate):
        if index == len(nums):
            result.append(slate[:])
            return

        helper(nums, index + 1, slate)

        slate.append(nums[index])
        helper(nums, index + 1, slate)
        slate.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(subsets([0]))
