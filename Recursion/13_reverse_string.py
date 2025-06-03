def reverse_from_left_to_right(string):
    """
    Reverses a string using a decrease-and-conquer strategy (left to right).
    """

    def helper(string, index):
        if index == len(string):
            return ""

        return helper(string, index + 1) + string[index]

    return helper(string, 0)


def reverse_from_right_to_left(string):
    """
    Reverses a string using a decrease-and-conquer strategy (right to left).
    """

    def helper(string, index):
        if index < 0:
            return ""

        return string[index] + helper(string, index - 1)

    return helper(string, len(string) - 1)


def reverse_divide_and_conquer(string):
    """
    Reverses a string using a divide-and-conquer strategy.
    """

    def helper(string, start, end):
        if start == end:
            return string[start]

        mid = start + (end - start) // 2
        return helper(string, mid + 1, end) + helper(string, start, mid)

    return helper(string, 0, len(string) - 1)


if __name__ == "__main__":
    string = "abcdefgh"
    print(reverse_from_left_to_right(string))
    print(reverse_from_right_to_left(string))
    print(reverse_divide_and_conquer(string))
