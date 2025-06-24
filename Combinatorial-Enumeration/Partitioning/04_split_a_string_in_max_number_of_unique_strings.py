def max_unique_split(s):
    def helper(s, i, slate):
        if len(slate) > 1 and len(slate) != len(set(slate)):
            return 0

        if i == len(s):
            return len(slate)

        largest = 0
        for end in range(i, len(s)):
            substring = s[i : end + 1]
            slate.append(substring)
            largest = max(largest, helper(s, end + 1, slate))
            slate.pop()

        return largest

    return helper(s, 0, [])


if __name__ == "__main__":
    print(max_unique_split("ababccc"))
    print(max_unique_split("aba"))
    print(max_unique_split("aa"))
