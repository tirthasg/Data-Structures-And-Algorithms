def partitions(num):
    def helper(s, i, slate):
        if i == len(s):
            result.append(slate[:])
            return

        for end in range(i, len(s)):
            substring = s[i : end + 1]
            slate.append(substring)
            helper(s, end + 1, slate)
            slate.pop()

    result = []
    helper(str(num), 0, [])
    return result


if __name__ == "__main__":
    print(partitions(123))
    print(partitions(100))
    print(partitions(21009))
    print(partitions(1))
    print(partitions(0))
