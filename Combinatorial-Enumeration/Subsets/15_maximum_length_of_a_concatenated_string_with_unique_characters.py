def max_length(arr):
    def helper(arr, i, slate):
        word = "".join(slate)
        if len(word) != len(set(word)):
            return 0

        if i == len(arr):
            return len(word)

        largest = helper(arr, i + 1, slate)

        slate.append(arr[i])
        largest = max(largest, helper(arr, i + 1, slate))
        slate.pop()

        return largest

    return helper(arr, 0, [])


if __name__ == "__main__":
    print(max_length(["un", "iq", "ue"]))
    print(max_length(["cha", "r", "act", "ers"]))
    print(max_length(["abcdefghijklmnopqrstuvwxyz"]))
