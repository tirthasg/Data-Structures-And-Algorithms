def disjoint_subsets(nums):
    def helper(nums, i, first, second):
        if i == len(nums):  # Leaf node worker / Base case
            result.append((first[:], second[:]))
            return

        # Internal node worker
        # Don't put the element in any of the two sets
        helper(nums, i + 1, first, second)

        # Put the element in the first set
        first.append(nums[i])
        helper(nums, i + 1, first, second)
        first.pop()

        # Put the element in the second set
        second.append(nums[i])
        helper(nums, i + 1, first, second)
        second.pop()

    result = []
    helper(nums, 0, [], [])
    return result


def disjoint_subsets_v2(nums):
    # A different enumeration strategy
    # We try to generate all subsets by fixing an element in the first set
    def helper(nums, i, first, second):
        # Every internal node worker writes down the partial solution into the global result
        # Every partial solution is a solution by itself
        result.append((first[:], second[:]))

        if i == len(nums):
            # Leaf node worker / Base case
            # Does nothing, apart from returning the control back to it's manager
            return

        for pick in range(i, len(nums)):
            # Add the element in the first set
            first.append(nums[pick])
            helper(nums, pick + 1, first, second)
            first.pop()

            # Add the element in the second set if the first set isn't empty
            if first:
                second.append(nums[pick])
                helper(nums, pick + 1, first, second)
                second.pop()

    result = []
    helper(nums, 0, [], [])
    return result


if __name__ == "__main__":
    print(disjoint_subsets([1, 2]))
    print(disjoint_subsets_v2([1, 2]))
    print(disjoint_subsets_v2([1, 1]))
    # print(disjoint_subsets([1, 2, 3]))
    # print(disjoint_subsets([1, 2, 2]))
    # print(disjoint_subsets([1, 2, 3, 4]))
    # print(disjoint_subsets([1, 2, 3, 4, 5]))
    # print(disjoint_subsets(list(range(11))))
