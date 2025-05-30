def print_hello_v1(n):
    # Using Decrease-and-conquer strategy from left
    def helper(n):
        if n == 0:
            return

        print("Hello", end=" ")
        helper(n - 1)

    helper(n)


def print_hello_v2(n):
    # Using Decrease-and-conquer strategy from right
    def helper(n):
        if n == 0:
            return

        helper(n - 1)
        print("Hello", end=" ")

    helper(n)


def print_hello_v3(n):
    # Using Divide-and-conquer strategy
    def helper(n):
        if n == 1:
            print("Hello", end=" ")
            return

        size1 = n // 2
        size2 = n - n // 2
        helper(size1)
        helper(size2)

    helper(n)


print_hello_v1(5)
print()

print_hello_v2(5)
print()

print_hello_v3(5)
print()
