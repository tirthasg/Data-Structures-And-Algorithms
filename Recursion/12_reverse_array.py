def reverse_left_to_right(nums):
    """
    Reverses an array using a decrease-and-conquer strategy (left to right).
    """

    def helper(nums, index):
        pair_index = len(nums) - 1 - index
        if index >= pair_index:
            return

        nums[index], nums[pair_index] = nums[pair_index], nums[index]
        helper(nums, index + 1)

    helper(nums, 0)


def reverse_right_to_left(nums):
    """
    Reverses an array using a decrease-and-conquer strategy (right to left).
    """

    def helper(nums, index):
        pair_index = len(nums) - 1 - index
        if pair_index >= index:
            return

        helper(nums, index - 1)
        nums[index], nums[pair_index] = nums[pair_index], nums[index]

    helper(nums, len(nums) - 1)


def reverse_divide_and_conquer(nums):
    """
    Reverses an array using a divide-and-conquer strategy.
    """

    def helper(nums, start, end):
        if start == end:
            return

        mid = start + (end - start) // 2
        helper(nums, start, mid)
        helper(nums, mid + 1, end)

        temp = []
        j = mid + 1
        while j <= end:
            temp.append(nums[j])
            j += 1

        i = start
        while i <= mid:
            temp.append(nums[i])
            i += 1

        k = 0
        while k < len(temp):
            nums[start + k] = temp[k]
            k += 1

    helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [3, 5, 1, 4, 2, 0]
    reverse_left_to_right(nums)
    print(nums)

    nums = [3, 5, 1, 4, 2, 0]
    reverse_right_to_left(nums)
    print(nums)

    nums = [3, 5, 1, 4, 2, 0]
    reverse_divide_and_conquer(nums)
    print(nums)
