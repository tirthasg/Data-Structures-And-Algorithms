def sum_from_right_to_left(num):
    """
    Sum of digits of a positive integer using a decrease-and-conquer strategy (right to left).
    """

    def helper(num):
        if 0 <= num <= 9:
            return num

        return num % 10 + helper(num // 10)

    return helper(num)


if __name__ == "__main__":
    print(sum_from_right_to_left(1001))
    print(sum_from_right_to_left(1000))
    print(sum_from_right_to_left(1234))
    print(sum_from_right_to_left(0))
    print(sum_from_right_to_left(6))
