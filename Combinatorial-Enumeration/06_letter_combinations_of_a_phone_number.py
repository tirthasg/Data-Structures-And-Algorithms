def letter_combinations(digits):
    def helper(digits, i, slate):
        if i == len(digits):
            result.append("".join(slate))
            return

        for choice in choices[digits[i]]:
            slate.append(choice)
            helper(digits, i + 1, slate)
            slate.pop()

    if not digits:
        return []

    choices = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    helper(digits, 0, [])
    return result


if __name__ == "__main__":
    print(letter_combinations("23"))
    print(letter_combinations(""))
    print(letter_combinations("2"))
