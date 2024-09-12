# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive version.
def postorder_traversal(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


# Iterative version.
def postorder_traversal1(root: TreeNode | None) -> list[int]:
    res: list[int] = []
    stack: list[TreeNode] = []
    prev, curr = None, root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack[-1]
            if not curr.right or curr.right == prev:
                stack.pop()
                res.append(curr.val)
                prev = curr
                curr = None
            else:
                curr = curr.right
    return res
