def print_hello_v1(n):
    # Using Decrease-and-conquer strategy from left
    if n == 0:
        return

    print("Hello", end=" ")
    print_hello_v1(n - 1)


def print_hello_v2(n):
    # Using Decrease-and-conquer strategy from right
    if n == 0:
        return

    print_hello_v2(n - 1)
    print("Hello", end=" ")


def print_hello_v3(n):
    # Using Divide-and-conquer strategy
    if n == 1:
        print("Hello", end=" ")
        return

    size1 = n // 2
    size2 = n - n // 2
    print_hello_v3(size1)
    print_hello_v3(size2)


print_hello_v1(5)
print()

print_hello_v2(5)
print()

print_hello_v3(5)
print()
