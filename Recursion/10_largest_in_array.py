def largest_from_left_to_right(nums):
    """
    Returns the largest element of the array using a decrease-and-conquer strategy (left to right).
    """

    def helper(nums, index):
        if index == len(nums):
            return nums[-1]

        return max(nums[index], helper(nums, index + 1))

    return helper(nums, 0)


def largest_from_right_to_left(nums):
    """
    Returns the largest element of the array using a decrease-and-conquer strategy (right to left).
    """

    def helper(nums, index):
        if index < 0:
            return nums[0]

        return max(helper(nums, index - 1), nums[index])

    return helper(nums, len(nums) - 1)


def largest_divide_and_conquer(nums):
    """
    Prints the largest element of the array using a divide-and-conquer strategy.
    """

    def helper(nums, start, end):
        if start == end:
            return nums[start]

        mid = start + (end - start) // 2
        return max(helper(nums, start, mid), helper(nums, mid + 1, end))

    return helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [3, 5, 1, 4, 2, 0]

    print(largest_from_left_to_right(nums))
    print(largest_from_right_to_left(nums))
    print(largest_divide_and_conquer(nums))
