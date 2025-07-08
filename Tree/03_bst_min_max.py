from tree_node import TreeNode


def find_min(root: TreeNode | None) -> int | None:
    if not root:
        return None

    curr = root
    while curr.left:
        curr = curr.left

    return curr.key


def find_max(root: TreeNode | None) -> int | None:
    if not root:
        return None

    curr = root
    while curr.right:
        curr = curr.right

    return curr.key


def find_minmax(root: TreeNode | None) -> tuple[int | None, int | None]:
    return find_min(root), find_max(root)


def insert(root: TreeNode | None, key: int) -> TreeNode | None:
    new_node = TreeNode(key)

    prev = None
    curr = root
    while curr:
        prev = curr
        if curr.key > key:
            curr = curr.left
        else:
            curr = curr.right

    if not prev:
        return new_node

    if prev.key > key:
        prev.left = new_node
    else:
        prev.right = new_node

    return root


if __name__ == "__main__":
    nums = [3, 5, 1, 4, 2, 0]
    root = None
    for num in nums:
        root = insert(root, num)

    print(find_minmax(root))
