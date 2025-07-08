from tree_node import TreeNode


def insert(root, key):
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


def search(root, key):
    curr = root
    while curr:
        if curr.key == key:
            return curr
        elif curr.key > key:
            curr = curr.left
        else:
            curr = curr.right

    return None


def find_min(root):
    if not root:
        return None

    curr = root
    while curr.left:
        curr = curr.left

    return curr.key


def find_successor(root, key):
    if not root:
        return None

    node = search(root, key)

    if node and node.right:
        return find_min(node.right)

    successor = None
    curr = root
    while curr != node:
        if curr.key > key:
            successor = curr
            curr = curr.left
        else:
            curr = curr.right

    return successor.key if successor else None


def find_max(root):
    if not root:
        return None

    curr = root
    while curr.right:
        curr = curr.right

    return curr.key


def find_predecessor(root, key):
    if not root:
        return None

    node = search(root, key)

    if node and node.left:
        return find_max(node.left)

    predecessor = None
    curr = root
    while curr != node:
        if curr.key > key:
            curr = curr.left
        else:
            predecessor = curr
            curr = curr.right

    return predecessor.key if predecessor else None


def find_predecessor_successor(root, key):
    if not root:
        return None, None

    return find_predecessor(root, key), find_successor(root, key)


if __name__ == "__main__":
    nums = [44, 17, 88, 8, 28, 65, 97, 29, 54, 82, 93, 76, 68, 80]
    root = None
    for num in nums:
        root = insert(root, num)

    print(find_predecessor_successor(root, 88))
    print(find_predecessor_successor(root, 97))
    print(find_predecessor_successor(root, 54))
    print(find_predecessor_successor(root, 53))
    print(find_predecessor_successor(root, 100))
