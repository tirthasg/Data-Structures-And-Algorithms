def letter_case_permutation(string):
    def helper(string, index, slate):
        if index == len(string):
            result.append("".join(slate))
            return

        if string[index].isdigit():
            slate.append(string[index])
            helper(string, index + 1, slate)
            slate.pop()
            return

        slate.append(string[index].lower())
        helper(string, index + 1, slate)
        slate.pop()

        slate.append(string[index].upper())
        helper(string, index + 1, slate)
        slate.pop()

    result = []
    helper(string, 0, [])
    return result


if __name__ == "__main__":
    print(letter_case_permutation("a1b2"))
    print(letter_case_permutation("3z4"))
    print(letter_case_permutation("12345"))
    print(letter_case_permutation("abcd"))
