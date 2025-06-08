def combination_sum_2_count(candidates, target):
    def helper(candidates, i, slate_sum):
        if slate_sum == target:
            return 1

        if slate_sum > target:
            return 0

        if i == len(candidates):
            return 0

        count = 0
        for pick in range(i, len(candidates)):
            if candidates[pick] != candidates[i]:
                break
            count += 1

        count_with_exclusion = helper(candidates, i + count, slate_sum)

        count_with_inclusion = 0
        for pick in range(count):
            count_with_inclusion += helper(
                candidates, i + count, slate_sum + (pick + 1) * candidates[i]
            )

        return count_with_exclusion + count_with_inclusion

    candidates.sort()
    return helper(candidates, 0, 0)


if __name__ == "__main__":
    print(combination_sum_2_count([10, 1, 2, 7, 6, 1, 5], target=8))
    print(combination_sum_2_count([2, 5, 2, 1, 2], target=5))
