def subsequences_with_duplicates(s):
    def helper(s, i, slate):
        result.append("".join(slate))

        if i == len(s):
            return

        uniques = set()
        for pick in range(i, len(s)):
            if s[pick] in uniques:
                continue
            uniques.add(s[pick])

            slate.append(s[pick])
            helper(s, pick + 1, slate)
            slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(subsequences_with_duplicates("abc"))
    print(subsequences_with_duplicates("abb"))
