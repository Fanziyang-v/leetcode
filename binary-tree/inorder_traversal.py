# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive version.
def inorder_traversal(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# Iterative version.
def inorder_traversal1(root: TreeNode | None) -> list[int]:
    res: list[int] = []
    stack: list[TreeNode] = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
    return res
