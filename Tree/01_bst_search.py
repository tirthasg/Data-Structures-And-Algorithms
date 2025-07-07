from tree_node import TreeNode


def search(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return None

    curr = root
    while curr:
        if curr.key == key:
            return curr
        elif curr.key > key:
            curr = curr.left
        else:
            curr = curr.right

    return None
