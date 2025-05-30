def power_v1(base, exponent):
    def helper(base, exponent):
        if exponent == 0:
            return 1

        return base * helper(base, exponent - 1)

    return helper(base, exponent)


def power_v2(base, exponent):
    def helper(base, exponent, curr):
        if curr > exponent:
            return 1

        return base * helper(base, exponent, curr + 1)

    return helper(base, exponent, 1)


def power_v3(base, exponent):
    def helper(base, low, high):
        if low == high:
            return base

        mid = low + (high - low) // 2
        return helper(base, low, mid) * helper(base, mid + 1, high)

    return helper(base, 1, exponent)


def power_v4(base, exponent):
    def helper(base, exponent):
        if exponent == 0:
            return 1

        half_power = helper(base, exponent // 2)
        result = half_power * half_power
        if exponent % 2 == 0:
            return result

        return base * result

    return helper(base, exponent)


print(power_v1(2, 5))
print(power_v2(2, 5))
print(power_v3(2, 5))
print(power_v4(2, 5))
