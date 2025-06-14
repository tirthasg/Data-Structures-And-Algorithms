def subsequences(s):
    def helper(s, i, slate):
        result.append("".join(slate))

        if i == len(s):
            return

        for pick in range(i, len(s)):
            slate.append(s[pick])
            helper(s, pick + 1, slate)
            slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(subsequences("abc"))
