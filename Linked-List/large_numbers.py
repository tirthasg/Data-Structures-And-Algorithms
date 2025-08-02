def add_large_numbers(nums1, nums2):
    result = []

    i = len(nums1) - 1
    j = len(nums2) - 1
    carry = 0

    while i >= 0 and j >= 0:
        curr_sum = nums1[i] + nums2[j] + carry
        result.append(curr_sum % 10)
        carry = curr_sum // 10

        i -= 1
        j -= 1

    while i >= 0:
        curr_sum = nums1[i] + carry
        result.append(curr_sum % 10)
        carry = curr_sum // 10

        i -= 1

    while j >= 0:
        curr_sum = nums2[j] + carry
        result.append(curr_sum % 10)
        carry = curr_sum // 10

        j -= 1

    if carry:
        result.append(carry)

    result.reverse()
    return result


def flip_nums(nums1, nums2):
    if len(nums1) < len(nums2):
        return True

    if len(nums1) > len(nums2):
        return False
    
    i = 0

    while i < len(nums1):
        if nums1[i] < nums2[i]:
            return True
        if nums1[i] > nums2[i]:
            return False
    
        i += 1

    return False
    

def subtract_large_numbers(nums1, nums2):
    negative = False
    if flip_nums(nums1, nums2):
        nums1, nums2 = nums2, nums1
        negative = True

    result = []

    i = len(nums1) - 1
    j = len(nums2) - 1
    borrow = 0

    while i >= 0 and j >= 0:
        curr_diff = nums1[i] - nums2[j] - borrow
        if curr_diff < 0:
            curr_diff += 10
            borrow = 1
        else:
            borrow = 0

        result.append(curr_diff)

        i -= 1
        j -= 1

    while i >= 0:
        curr_diff = nums1[i] - borrow
        if curr_diff < 0:
            curr_diff += 10
            borrow = 1
        else:
            borrow = 0

        result.append(curr_diff)
        i -= 1

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    if negative:
        result.append("-")

    result.reverse()

    return result


if __name__ == "__main__":
    print(add_large_numbers([1, 2, 3], [4, 5]))
    print(add_large_numbers([9, 9], [1]))
    print(
        add_large_numbers(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        )
    )

    print(subtract_large_numbers([1, 0, 0, 0], [1]))
    print(subtract_large_numbers([1, 2, 3], [4, 5, 6]))
    print(subtract_large_numbers([1], [1, 0, 0, 0]))
    print(subtract_large_numbers([1, 0, 0, 0, 0], [1]))
    print(subtract_large_numbers([7], [3, 3, 0]))
