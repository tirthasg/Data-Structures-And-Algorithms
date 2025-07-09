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


def delete_leaf(root, prev, curr):
    if not prev:
        return None

    if prev.left == curr:
        prev.left = None
    else:
        prev.right = None

    return root


def delete_node_with_one_child(root, prev, curr):
    child = curr.left if curr.left else curr.right

    if not prev:
        return child

    if prev.left == curr:
        prev.left = child
    else:
        prev.right = child

    return root


def delete_node_with_two_children(root, prev, curr):
    prev = curr
    successor = curr.right
    while successor.left:
        prev = successor
        successor = successor.left

    curr.key = successor.key
    if prev.left == successor:
        prev.left = successor.right
    else:
        prev.right = successor.right


def delete(root, key):
    prev = None
    curr = root
    while curr:
        if curr.key == key:
            break
        elif curr.key > key:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right

    if not curr:
        return root

    if not curr.left and not curr.right:
        return delete_leaf(root, prev, curr)

    if (curr.left and not curr.right) or (not curr.left and curr.right):
        return delete_node_with_one_child(root, prev, curr)

    return delete_node_with_two_children(root, prev, curr)


if __name__ == "__main__":
    nums = [44, 17, 88, 8, 28, 65, 97, 29, 54, 82, 93, 76, 68, 80]
    root = None
    for num in nums:
        root = insert(root, num)

    for num in nums:
        root = delete(root, num)

    print(root)
