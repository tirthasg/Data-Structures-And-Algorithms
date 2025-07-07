from tree_node import TreeNode


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