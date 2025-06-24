def partitions(n):
    def helper(i, slate, slate_sum):
        if slate_sum > n:
            return

        if slate_sum == n:
            result.append(slate[:])
            return

        if i == n:
            return

        helper(i + 1, slate, slate_sum)

        max_frequency = n // i
        for freq in range(1, max_frequency + 1):
            slate.append(i)
            helper(i + 1, slate, slate_sum + freq * i)

        for _ in range(max_frequency):
            slate.pop()

    result = []
    helper(1, [], 0)
    return result


if __name__ == "__main__":
    print(partitions(4))
    print(partitions(5))
    print(partitions(1))
