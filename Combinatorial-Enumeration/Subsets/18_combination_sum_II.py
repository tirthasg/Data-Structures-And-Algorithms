def combination_sum2(candidates, target):
    def helper(candidates, i, slate, slate_sum):
        if slate_sum > target:
            return

        if slate_sum == target:
            result.append(slate[:])
            return

        if i == len(candidates):
            return

        count = 0
        for pick in range(i, len(candidates)):
            if candidates[pick] != candidates[i]:
                break
            count += 1

        helper(candidates, i + count, slate, slate_sum)

        for freq in range(1, count + 1):
            slate.append(candidates[i])
            helper(candidates, i + count, slate, slate_sum + freq * candidates[i])

        for _ in range(count):
            slate.pop()

    candidates.sort(reverse=True)
    result = []
    helper(candidates, 0, [], 0)
    return result


def combination_sum2_v2(candidates, target):
    def helper(candidates, i, slate, slate_sum):
        if slate_sum > target:
            return

        if slate_sum == target:
            result.append(slate[:])

        if i == len(candidates):
            return

        uniques = set()
        for pick in range(i, len(candidates)):
            if candidates[pick] in uniques:
                continue
            uniques.add(candidates[pick])

            slate.append(candidates[pick])
            helper(candidates, pick + 1, slate, slate_sum + candidates[pick])
            slate.pop()

    candidates.sort(reverse=True)
    result = []
    helper(candidates, 0, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum2([10, 1, 2, 7, 6, 1, 5], target=8))
    print(combination_sum2([2, 5, 2, 1, 2], target=5))
    print()
    print(combination_sum2_v2([10, 1, 2, 7, 6, 1, 5], target=8))
    print(combination_sum2_v2([2, 5, 2, 1, 2], target=5))
