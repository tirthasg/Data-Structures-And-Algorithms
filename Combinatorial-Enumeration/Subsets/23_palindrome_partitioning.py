def parition(s):
    def helper(s, i, slate):
        if len(slate) > 0 and slate[-1] != slate[-1][::-1]:
            return

        if i == len(s):
            result.append(slate[:])
            return

        for end in range(i, len(s)):
            substring = s[i : end + 1]
            slate.append(substring)
            helper(s, end + 1, slate)
            slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(parition("aab"))
    print(parition("a"))
