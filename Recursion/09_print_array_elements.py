def print_from_left_to_right(nums):
    """
    Prints the array elements using a decrease-and-conquer strategy (left to right).
    """

    def helper(nums, index):
        if index == len(nums):
            return

        print(nums[index], end=" ")
        helper(nums, index + 1)

    helper(nums, 0)


def print_from_right_to_left(nums):
    """
    Prints the array elements using a decrease-and-conquer strategy (right to left).
    """

    def helper(nums, index):
        if index < 0:
            return

        helper(nums, index - 1)
        print(nums[index], end=" ")

    helper(nums, len(nums) - 1)


def print_divide_and_conquer(nums):
    """
    Prints the array elements using a divide-and-conquer strategy.
    """

    def helper(nums, low, high):
        if low == high:
            print(nums[low], end=" ")
            return

        mid = low + (high - low) // 2
        helper(nums, low, mid)
        helper(nums, mid + 1, high)

    helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [3, 5, 1, 4, 2, 0]

    print_from_left_to_right(nums)
    print()

    print_from_right_to_left(nums)
    print()

    print_divide_and_conquer(nums)
    print()
