def copy_from_left_to_right(chars):
    """
    Copy contents of a char array into another using a decrease-and-conquer strategy (left to right).
    """

    def helper(chars, index, result):
        if index == len(chars):
            return

        result[index] += chars[index]
        helper(chars, index + 1, result)

    result = [""] * len(chars)
    helper(chars, 0, result)
    return result


def copy_from_right_to_left(chars):
    """
    Copy contents of a char array into another using a decrease-and-conquer strategy (right to left).
    """

    def helper(chars, index, result):
        if index < 0:
            return

        helper(chars, index - 1, result)
        result[index] += chars[index]

    result = [""] * len(chars)
    helper(chars, len(chars) - 1, result)
    return result


def copy_divide_and_conquer(chars):
    """
    Copy contents of a char array into another using a divide-and-conquer strategy.
    """

    def helper(chars, start, end, result):
        if start == end:
            result[start] += chars[start]
            return

        mid = start + (end - start) // 2
        helper(chars, start, mid, result)
        helper(chars, mid + 1, end, result)

    result = [""] * len(chars)
    helper(chars, 0, len(chars) - 1, result)
    return result


if __name__ == "__main__":
    chars = list("abcdefgh")
    print(copy_from_left_to_right(chars))
    print(copy_from_right_to_left(chars))
    print(copy_divide_and_conquer(chars))
