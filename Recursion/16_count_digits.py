def count_from_right_to_left(num):
    """
    Count digits in a positive integer using a decrease-and-conquer strategy (right to left).
    """

    def helper(num):
        if 0 <= num <= 9:
            return 1

        return 1 + helper(num // 10)

    return helper(num)


if __name__ == "__main__":
    print(count_from_right_to_left(1001))
    print(count_from_right_to_left(1000))
    print(count_from_right_to_left(1234))
    print(count_from_right_to_left(0))
    print(count_from_right_to_left(6))
