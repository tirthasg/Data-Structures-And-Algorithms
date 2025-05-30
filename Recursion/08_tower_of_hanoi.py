def tower_of_hanoi(n, src, dest, aux):
    def helper(n, src, dest, aux):
        if n == 0:
            return

        helper(n - 1, src, aux, dest)
        print(f"Moving disc from {src} to {dest}")
        helper(n - 1, aux, dest, src)

    helper(n, src, dest, aux)


tower_of_hanoi(3, 1, 2, 3)
