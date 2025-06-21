def partitions(nums):
    def helper(nums, i, slate):
        if i == len(nums):
            result.append([subset[:] for subset in slate])
            return

        slate.append([nums[i]])
        helper(nums, i + 1, slate)
        slate.pop()

        for pick in range(len(slate)):
            subset = slate[pick]
            subset.append(nums[i])
            helper(nums, i + 1, slate)
            subset.pop()

    result = []
    helper(nums, 0, [])
    return result


if __name__ == "__main__":
    print(partitions([1, 2, 3]))
    print(partitions([1]))


# https://leetcode.com/problems/block-placement-queries
# https://leetcode.com/problems/maximize-the-minimum-game-score
# https://leetcode.com/problems/maximum-number-of-robots-within-budget
# https://leetcode.com/problems/maximum-profit-in-job-scheduling
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals
# https://leetcode.com/problems/minimum-cost-to-make-array-equal

# https://leetcode.com/problems/avoid-flood-in-the-city
# https://leetcode.com/problems/closest-equal-element-queries
# https://leetcode.com/problems/find-k-closest-elements
# https://leetcode.com/problems/k-th-smallest-prime-fraction
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
# https://leetcode.com/problems/maximum-points-inside-the-square
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs
