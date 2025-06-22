def is_additive_number(num):
    def helper(num, i, slate):
        if len(slate) > 2:
            curr = slate[-1]
            prev = slate[-2]
            prev_of_prev = slate[-3]

            if curr[0] == "0" and len(curr) > 1:
                return False

            if prev[0] == "0" and len(prev) > 1:
                return False

            if prev_of_prev[0] == "0" and len(prev_of_prev) > 1:
                return False

            if int(curr) != int(prev) + int(prev_of_prev):
                return False

        if i == len(num):
            return len(slate) > 2

        for end in range(i, len(num)):
            substring = num[i : end + 1]
            slate.append(substring)
            if helper(num, end + 1, slate):
                return True
            slate.pop()

        return False

    if len(num) < 3:
        return False

    return helper(num, 0, [])


if __name__ == "__main__":
    print(is_additive_number("112358"))
    print(is_additive_number("199100199"))
    print(is_additive_number("1023"))
    print(is_additive_number("000"))
    print(is_additive_number("0"))
