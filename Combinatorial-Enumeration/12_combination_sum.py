def combination_sum(candidates, target):
    def helper(candidates, i, slate):
        if sum(slate) == target:
            result.append(slate[:])
            return

        if sum(slate) > target:
            return

        if i == len(candidates):
            return

        helper(candidates, i + 1, slate)

        max_frequency = target // candidates[i]
        for _ in range(max_frequency):
            slate.append(candidates[i])
            helper(candidates, i + 1, slate)

        for _ in range(max_frequency):
            slate.pop()

    result = []
    helper(candidates, 0, [])
    return result


def combination_sum_with_optimization(candidates, target):
    def helper(candidates, i, slate, slate_sum):
        if slate_sum == target:
            result.append(slate[:])
            return

        if slate_sum > target:
            return

        if i == len(candidates):
            return

        helper(candidates, i + 1, slate, slate_sum)

        max_frequency = target // candidates[i]
        for frequency in range(max_frequency):
            slate.append(candidates[i])
            helper(
                candidates, i + 1, slate, slate_sum + (frequency + 1) * candidates[i]
            )

        for _ in range(max_frequency):
            slate.pop()

    result = []
    helper(candidates, 0, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], target=7))
    print(combination_sum([2, 3, 5], target=8))
    print(combination_sum([2], target=1))

    print(combination_sum_with_optimization([2, 3, 6, 7], target=7))
    print(combination_sum_with_optimization([2, 3, 5], target=8))
    print(combination_sum_with_optimization([2], target=1))
