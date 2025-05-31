def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Prints the sequence of moves involved in the Tower of Hanoi problem for n disks to transfer all disks from source to destination.
    """

    def helper(n, src, dest, aux):
        if n == 0:
            return

        helper(n - 1, src, aux, dest)
        print(f"Move disk {n} from {src} to {dest}")
        helper(n - 1, aux, dest, src)

    helper(n, source, destination, auxiliary)


if __name__ == "__main__":
    tower_of_hanoi(3, "A", "C", "B")
