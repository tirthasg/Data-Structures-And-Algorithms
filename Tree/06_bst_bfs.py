from tree_node import TreeNode
from queue import Queue


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


def bfs(root):
    q = Queue()
    q.put(root)

    while q.qsize():
        node = q.get()
        print(node.key, end=" ")

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    print()


def dfs(root):
    def helper(root):
        if not root:
            return

        print(root.key, end=" ")
        helper(root.left)
        helper(root.right)

    helper(root)
    print()


if __name__ == "__main__":
    nums = [44, 17, 88, 8, 28, 65, 97, 29, 54, 82, 93, 76, 68, 80]
    root = None
    for num in nums:
        root = insert(root, num)

    bfs(root)
    dfs(root)
