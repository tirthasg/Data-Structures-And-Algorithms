def combination_sum(candidates, target):
    def helper(candidates, i, slate, slate_sum):
        if slate_sum > target:
            return

        if slate_sum == target:
            result.append(slate[:])
            return

        if i == len(candidates):
            return

        helper(candidates, i + 1, slate, slate_sum)

        max_frequency = target // candidates[i]
        for frequency in range(1, max_frequency + 1):
            slate.append(candidates[i])
            helper(candidates, i + 1, slate, slate_sum + frequency * candidates[i])

        for _ in range(max_frequency):
            slate.pop()

    candidates.sort(reverse=True)
    result = []
    helper(candidates, 0, [], 0)
    return result


def combination_sum_v2(candidates, target):
    def helper(candidates, i, slate, slate_sum):
        if slate_sum > target:
            return

        if slate_sum == target:
            result.append(slate[:])
            return

        if i == len(candidates):
            return

        for pick in range(i, len(candidates)):
            max_frequency = target // candidates[pick]
            for freq in range(1, max_frequency + 1):
                slate.append(candidates[pick])
                helper(candidates, pick + 1, slate, slate_sum + freq * candidates[pick])

            for _ in range(max_frequency):
                slate.pop()

    candidates.sort(reverse=True)
    result = []
    helper(candidates, 0, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], target=7))
    print(combination_sum([2, 3, 5], target=8))
    print(combination_sum([2], target=1))
    print()
    print(combination_sum_v2([2, 3, 6, 7], target=7))
    print(combination_sum_v2([2, 3, 5], target=8))
    print(combination_sum_v2([2], target=1))
