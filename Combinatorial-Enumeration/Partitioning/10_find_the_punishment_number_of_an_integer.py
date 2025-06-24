def punishment_number(n):
    def helper(s, i, slate_sum, pick):
        if slate_sum > pick:
            return False

        if i == len(s):
            return slate_sum == pick

        for end in range(i, len(s)):
            substring = s[i : end + 1]
            if helper(s, end + 1, slate_sum + int(substring), pick):
                return True

        return False

    count = 0
    for pick in range(1, n + 1):
        if (pick % 9 == 0 or pick % 9 == 1) and helper(str(pick * pick), 0, 0, pick):
            count += pick * pick

    return count


if __name__ == "__main__":
    print(punishment_number(10))
    print(punishment_number(37))
