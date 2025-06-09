def combination_sum_2_decision(candidates, target):
    def helper(candidates, i, slate_sum):
        if slate_sum == target:
            return True

        if slate_sum > target:
            return False

        if i == len(candidates):
            return False

        count = 0
        for pick in range(i, len(candidates)):
            if candidates[pick] != candidates[i]:
                break
            count += 1

        if helper(candidates, i + count, slate_sum):
            return True

        for pick in range(count):
            if helper(candidates, i + count, slate_sum + (pick + 1) * candidates[i]):
                return True

        return False

    candidates.sort()
    return helper(candidates, 0, 0)


if __name__ == "__main__":
    print(combination_sum_2_decision([10, 1, 2, 7, 6, 1, 5], target=8))
    print(combination_sum_2_decision([2, 5, 2, 1, 2], target=5))
    print(combination_sum_2_decision([2, 5, 2, 1, 2], target=50))
    print(combination_sum_2_decision([1, 3, 5, 7], target=2))
