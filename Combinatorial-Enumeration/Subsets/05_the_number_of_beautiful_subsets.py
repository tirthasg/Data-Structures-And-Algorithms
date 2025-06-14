def beautiful_subsets_v1(nums, k):
    def helper(nums, i, slate):
        if len(slate) > 1:
            last = slate[-1]
            uniques = set(slate)
            if last - k in uniques or last + k in uniques:
                return

        if i == len(nums):
            result.append(slate[:])
            return

        helper(nums, i + 1, slate)

        slate.append(nums[i])
        helper(nums, i + 1, slate)
        slate.pop()

    result = []
    helper(nums, 0, [])
    return len(result) - 1


def beautiful_subsets_v2(nums, k):
    def helper(nums, i, slate):
        if len(slate) > 1:
            last = slate[-1]
            uniques = set(slate)
            if last + k in uniques or last - k in uniques:
                return 0

        if i == len(nums):
            return 1

        count = helper(nums, i + 1, slate)

        slate.append(nums[i])
        count += helper(nums, i + 1, slate)
        slate.pop()

        return count

    return helper(nums, 0, []) - 1


def beautiful_subsets_v3(nums, k):
    def helper(nums, i, slate):
        if len(slate) > 1:
            last = slate[-1]
            uniques = set(slate)
            if last - k in uniques:
                return 0

        if i == len(nums):
            return 1

        count = helper(nums, i + 1, slate)

        slate.append(nums[i])
        count += helper(nums, i + 1, slate)
        slate.pop()

        return count

    nums.sort()
    return helper(nums, 0, []) - 1


def beautiful_subsets_v4(nums, k):
    def helper(nums, i, slate, uniques):
        if len(slate) > 1:
            last = slate[-1]
            if last - k in uniques:
                return 0

        if i == len(nums):
            return 1

        count = helper(nums, i + 1, slate, uniques)

        slate.append(nums[i])
        count += helper(nums, i + 1, slate, uniques | {nums[i]})
        slate.pop()

        return count

    nums.sort()
    return helper(nums, 0, [], set()) - 1


def beautiful_subsets_v5(nums, k):
    def helper(nums, i, slate, uniques):
        if len(slate) > 1:
            last = slate[-1]
            if uniques.get(last - k):
                return 0

        if i == len(nums):
            return 1

        count = helper(nums, i + 1, slate, uniques)

        slate.append(nums[i])
        uniques[nums[i]] = uniques.setdefault(nums[i], 0) + 1
        count += helper(nums, i + 1, slate, uniques)
        uniques[nums[i]] -= 1

        return count

    nums.sort()
    return helper(nums, 0, [], dict()) - 1


def beautiful_subsets_v6(nums, k):
    def helper(nums, i, uniques):
        if i == len(nums):
            return 1

        count = helper(nums, i + 1, uniques)

        if not uniques.get(nums[i] - k):
            uniques[nums[i]] = uniques.setdefault(nums[i], 0) + 1
            count += helper(nums, i + 1, uniques)
            uniques[nums[i]] -= 1

        return count

    nums.sort()
    return helper(nums, 0, dict()) - 1


if __name__ == "__main__":
    print(beautiful_subsets_v1([2, 4, 6], k=2))
    print(beautiful_subsets_v1([1], k=1))
    print(beautiful_subsets_v1([18, 10, 18], k=8))
    print()
    print(beautiful_subsets_v2([2, 4, 6], k=2))
    print(beautiful_subsets_v2([1], k=1))
    print(beautiful_subsets_v2([18, 10, 18], k=8))
    print()
    print(beautiful_subsets_v3([2, 4, 6], k=2))
    print(beautiful_subsets_v3([1], k=1))
    print(beautiful_subsets_v3([18, 10, 18], k=8))
    print()
    print(beautiful_subsets_v4([2, 4, 6], k=2))
    print(beautiful_subsets_v4([1], k=1))
    print(beautiful_subsets_v4([18, 10, 18], k=8))
    print()
    print(beautiful_subsets_v5([2, 4, 6], k=2))
    print(beautiful_subsets_v5([1], k=1))
    print(beautiful_subsets_v5([18, 10, 18], k=8))
    print()
    print(beautiful_subsets_v6([2, 4, 6], k=2))
    print(beautiful_subsets_v6([1], k=1))
    print(beautiful_subsets_v6([18, 10, 18], k=8))
