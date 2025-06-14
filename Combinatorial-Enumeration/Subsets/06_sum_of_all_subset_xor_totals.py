from functools import reduce


def subset_xor_sum_v1(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            return reduce(lambda x, y: x ^ y, slate, 0)

        total = helper(nums, i + 1, slate)

        slate.append(nums[i])
        total += helper(nums, i + 1, slate)
        slate.pop()

        return total

    return helper(nums, 0, [])


def subset_xor_sum_v2(nums):
    def helper(nums, i, xor_total):
        if i == len(nums):
            return xor_total

        return helper(nums, i + 1, xor_total) + helper(nums, i + 1, xor_total ^ nums[i])

    return helper(nums, 0, 0)


if __name__ == "__main__":
    print(subset_xor_sum_v1([1, 3]))
    print(subset_xor_sum_v1([5, 1, 6]))
    print(subset_xor_sum_v1([3, 4, 5, 6, 7, 8]))
    print()
    print(subset_xor_sum_v2([1, 3]))
    print(subset_xor_sum_v2([5, 1, 6]))
    print(subset_xor_sum_v2([3, 4, 5, 6, 7, 8]))
