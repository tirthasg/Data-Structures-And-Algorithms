def subsequences(s):
    def helper(s, i, slate):
        if i == len(s):
            result.append("".join(slate))
            return

        helper(s, i + 1, slate)

        slate.append(s[i])
        helper(s, i + 1, slate)
        slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(subsequences("abc"))
