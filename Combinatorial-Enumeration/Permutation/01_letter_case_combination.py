def letter_case_permutation(s):
    def helper(s, i, slate):
        if i == len(s):
            result.append("".join(slate))
            return

        if s[i].isdigit():
            slate.append(s[i])
            helper(s, i + 1, slate)
            slate.pop()
            return

        slate.append(s[i].lower())
        helper(s, i + 1, slate)
        slate.pop()

        slate.append(s[i].upper())
        helper(s, i + 1, slate)
        slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(letter_case_permutation("a1b2"))
    print(letter_case_permutation("3z4"))
    print(letter_case_permutation("12345"))
    print(letter_case_permutation("abcd"))
