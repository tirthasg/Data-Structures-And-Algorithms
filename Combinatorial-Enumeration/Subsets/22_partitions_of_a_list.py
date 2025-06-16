def partitions(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
            return

        for end in range(i, len(nums)):
            sublist = nums[i : end + 1]
            slate.append(sublist)
            helper(nums, end + 1, slate)
            slate.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(partitions([1, 2, 3]))
