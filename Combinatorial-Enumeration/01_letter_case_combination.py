def letter_case_permutation(s):
    def helper(s, index, slate):
        if index == len(s):
            result.append("".join(slate))
            return

        if s[index].isdigit():
            slate.append(s[index])
            helper(s, index + 1, slate)
            slate.pop()
            return

        slate.append(s[index].lower())
        helper(s, index + 1, slate)
        slate.pop()

        slate.append(s[index].upper())
        helper(s, index + 1, slate)
        slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(letter_case_permutation("a1b2"))
    print(letter_case_permutation("3z4"))
    print(letter_case_permutation("12345"))
    print(letter_case_permutation("abcd"))
