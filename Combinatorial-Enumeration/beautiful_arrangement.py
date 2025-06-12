def count_arrangement(n):
    def helper(digits, i, slate):
        if len(slate) > 0:
            prev = slate[-1]
            label = i
            if not (prev % label == 0 or label % prev == 0):
                return 0

        if i == n:
            return 1

        count = 0
        for pick in range(i, len(digits)):
            digits[i], digits[pick] = digits[pick], digits[i]
            slate.append(digits[i])
            count += helper(digits, i + 1, slate)
            slate.pop()
            digits[i], digits[pick] = digits[pick], digits[i]

        return count

    return helper(list(range(1, n + 1)), 0, [])


if __name__ == "__main__":
    print(count_arrangement(2))
    print(count_arrangement(1))
