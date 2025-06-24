def partitions(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append([subset[:] for subset in slate])
            return

        slate.append([nums[i]])
        helper(nums, i + 1, slate)
        slate.pop()

        for pick in range(len(slate)):
            subset = slate[pick]
            subset.append(nums[i])
            helper(nums, i + 1, slate)
            subset.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(partitions([1, 2, 3]))
    print(partitions([1]))
