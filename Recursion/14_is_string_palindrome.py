def check_from_left_to_right(string):
    """
    Checks whether a string forms a palindrome using a decrease-and-conquer strategy (left to right).
    """

    def helper(string, index):
        pair_index = len(string) - 1 - index
        if index >= pair_index:
            return True

        if string[index] == string[pair_index]:
            return helper(string, index + 1)

        return False

    return helper(string, 0)


def check_from_right_to_left(string):
    """
    Checks whether a string forms a palindrome using a decrease-and-conquer strategy (right to left).
    """

    def helper(string, index):
        pair_index = len(string) - 1 - index
        if pair_index >= index:
            return True

        left_answer = helper(string, index - 1)
        if not left_answer:
            return False

        return string[index] == string[pair_index]

    return helper(string, len(string) - 1)


if __name__ == "__main__":
    print(check_from_left_to_right("racecar"))
    print(check_from_right_to_left("racecar"))

    print(check_from_left_to_right("abcd"))
    print(check_from_right_to_left("abcd"))
