def gray_code_bfs(n):
    def helper(n):
        if n == 1:
            return ["0", "1"]

        prev = helper(n - 1)
        starts_with_zero = ["0" + code for code in prev]
        starts_with_one = ["1" + code for code in reversed(prev)]

        return starts_with_zero + starts_with_one

    return helper(n)


def gray_code_dfs(n):
    def helper(i, slate):
        if i == n:
            result.append("".join(slate))
            return

        xor = 0
        for ele in slate:
            xor ^= int(ele)

        slate.append(str(xor))
        helper(i + 1, slate)
        slate.pop()

        slate.append(str(1 - xor))
        helper(i + 1, slate)
        slate.pop()

    result = []
    helper(0, [])
    return result


def gray_code_dfs_with_optimization(n):
    def helper(i, slate, slate_xor):
        if i == n:
            result.append("".join(slate))
            return

        slate.append(str(slate_xor))
        helper(i + 1, slate, 0)
        slate.pop()

        slate.append(str(1 - slate_xor))
        helper(i + 1, slate, 1)
        slate.pop()

    result = []
    helper(0, [], 0)
    return result


if __name__ == "__main__":
    print(gray_code_bfs(1))
    print(gray_code_dfs(1))
    print(gray_code_dfs_with_optimization(1))

    print(gray_code_bfs(2))
    print(gray_code_dfs(2))
    print(gray_code_dfs_with_optimization(2))

    print(gray_code_bfs(3))
    print(gray_code_dfs(3))
    print(gray_code_dfs_with_optimization(3))
