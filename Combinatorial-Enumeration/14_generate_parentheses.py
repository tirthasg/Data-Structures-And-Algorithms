def generate_parentheses(n):
    def helper(left, right, slate):
        if left > right:
            return

        if left == 0 and right == 0:
            result.append("".join(slate))
            return

        if left > 0:
            slate.append("(")
            helper(left - 1, right, slate)
            slate.pop()

        if right > 0:
            slate.append(")")
            helper(left, right - 1, slate)
            slate.pop()

    result = []
    helper(n, n, [])
    return result


if __name__ == "__main__":
    print(generate_parentheses(3))
    print(generate_parentheses(1))
