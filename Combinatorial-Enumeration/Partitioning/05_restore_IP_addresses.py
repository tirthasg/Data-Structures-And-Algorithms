def restore_ip_addresses(s):
    def helper(s, i, slate):
        if slate:
            if len(slate) > 4:
                return

            last = slate[-1]
            if last[0] == "0" and len(last) > 1:
                return

            if int(last) > 255:
                return

        if i == len(s):
            if len(slate) == 4:
                result.append(".".join(slate))
            return

        for end in range(i, len(s)):
            substring = s[i : end + 1]
            slate.append(substring)
            helper(s, end + 1, slate)
            slate.pop()

    result = []
    helper(s, 0, [])
    return result


if __name__ == "__main__":
    print(restore_ip_addresses("25525511135"))
    print(restore_ip_addresses("0000"))
    print(restore_ip_addresses("101023"))
