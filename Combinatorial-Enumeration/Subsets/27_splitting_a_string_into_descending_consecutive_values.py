def split_string(s):
    def helper(s, i, slate):
        if len(slate) > 1:
            curr = int(slate[-1])
            prev = int(slate[-2])
            if prev <= curr or prev - curr != 1:
                return False

        if i == len(s):
            return len(slate) > 1

        for end in range(i, len(s)):
            substring = s[i : end + 1]
            slate.append(substring)
            if helper(s, end + 1, slate):
                return True
            slate.pop()

        return False

    if len(s) < 2:
        return False

    return helper(s, 0, [])


if __name__ == "__main__":
    print(split_string("1234"))
    print(split_string("050043"))
    print(split_string("9080701"))
