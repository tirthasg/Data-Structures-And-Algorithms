def combination_sum_2(candidates, target):
    def helper(candidates, i, slate):
        if sum(slate) == target:
            result.append(slate[:])
            return

        if sum(slate) > target:
            return

        if i == len(candidates):
            return

        count = 0
        for pick in range(i, len(candidates)):
            if candidates[pick] != candidates[i]:
                break
            count += 1

        helper(candidates, i + count, slate)

        for _ in range(count):
            slate.append(candidates[i])
            helper(candidates, i + count, slate)

        for _ in range(count):
            slate.pop()

    candidates.sort()

    result = []
    helper(candidates, 0, [])
    return result


def combination_sum_2_with_optimization(candidates, target):
    def helper(candidates, i, slate, slate_sum):
        if slate_sum == target:
            result.append(slate[:])
            return

        if slate_sum > target:
            return

        if i == len(candidates):
            return

        count = 0
        for pick in range(i, len(candidates)):
            if candidates[pick] != candidates[i]:
                break
            count += 1

        helper(candidates, i + count, slate, slate_sum)

        for pick in range(count):
            slate.append(candidates[i])
            helper(candidates, i + count, slate, slate_sum + (pick + 1) * candidates[i])

        for _ in range(count):
            slate.pop()

    candidates.sort()

    result = []
    helper(candidates, 0, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum_2([10, 1, 2, 7, 6, 1, 5], target=8))
    print(combination_sum_2([2, 5, 2, 1, 2], target=5))

    print(combination_sum_2_with_optimization([10, 1, 2, 7, 6, 1, 5], target=8))
    print(combination_sum_2_with_optimization([2, 5, 2, 1, 2], target=5))
