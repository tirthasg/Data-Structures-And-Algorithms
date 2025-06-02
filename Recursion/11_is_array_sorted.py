def check_from_left_to_right(nums):
    """
    Checks whether array is sorted using a decrease-and-conquer strategy (left to right).
    """

    def helper(nums, index):
        if index == len(nums) - 1:
            return True

        if nums[index] <= nums[index + 1]:
            return helper(nums, index + 1)

        return False

    return helper(nums, 0)


def check_from_right_to_left(nums):
    """
    Checks whether array is sorted using a decrease-and-conquer strategy (right to left).
    """

    def helper(nums, index):
        if index == 0:
            return True

        if helper(nums, index - 1):
            return nums[index - 1] <= nums[index]

        return False

    return helper(nums, len(nums) - 1)


def check_divide_and_conquer(nums):
    """
    Checks whether array is sorted using a divide-and-conquer strategy.
    """

    def helper(nums, start, end):
        if start == end:
            return True

        mid = start + (end - start) // 2
        left_answer = helper(nums, start, mid)
        if not left_answer:
            return False

        right_answer = helper(nums, mid + 1, end)
        if not right_answer:
            return False

        return nums[mid] <= nums[mid + 1]

    return helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [3, 5, 1, 4, 2, 0]
    print(check_from_left_to_right(nums))
    print(check_from_right_to_left(nums))
    print(check_divide_and_conquer(nums))

    nums = [0, 1, 2, 3, 4, 5]
    print(check_from_left_to_right(nums))
    print(check_from_right_to_left(nums))
    print(check_divide_and_conquer(nums))

    nums = [-3, -1, 0, 1, 2, 5, 5, 6, 10]
    print(check_from_left_to_right(nums))
    print(check_from_right_to_left(nums))
    print(check_divide_and_conquer(nums))
