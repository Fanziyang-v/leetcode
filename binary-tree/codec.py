"""
Serialize and Deserialize Binary Tree.

Link: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


NULL = 'null'
SEPARATOR = ','

# Using binary tree preorder traversal.
class Codec:

    def serialize(self, root: TreeNode | None) -> str:
        lst: list[str] = []
        def traverse(root: TreeNode | None) -> None:
            nonlocal lst
            if root is None:
                lst.append(NULL)
                return
            lst.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return SEPARATOR.join(lst)
    

    def deserialize(self, data: str) -> TreeNode | None:
        lst = data.split(SEPARATOR)
        def traverse() -> TreeNode | None:
            nonlocal lst
            item = lst.pop(0)
            if item == NULL:
                return None
            root = TreeNode(int(item))
            root.left = traverse()
            root.right = traverse()
            return root
        return traverse()


# Using binary tree postorder traversal.
class Codec1:

    def serialize(self, root: TreeNode | None) -> str:
        lst: list[str] = []
        def traverse(root: TreeNode | None) -> None:
            nonlocal lst
            if root is None:
                lst.append(NULL)
                return
            traverse(root.left)
            traverse(root.right)
            lst.append(str(root.val))
        traverse(root)
        return SEPARATOR.join(lst)
    

    def deserialize(self, data: str) -> TreeNode | None:
        lst = data.split(SEPARATOR)
        def traverse() -> TreeNode | None:
            nonlocal lst
            item = lst.pop()
            if item == NULL:
                return None
            root = TreeNode(int(item))
            root.right = traverse()
            root.left = traverse()
            return root
        return traverse()


# Using binary tree level order traversal.
class Codec2:

    def serialize(self, root: TreeNode | None) -> str:
        if root is None:
            return ""
        layer = [root]
        lst: list[str] = []
        while layer:
            next_layer: list[TreeNode | None] = []
            for node in layer:
                lst.append(NULL if node is None else str(node.val))
                if node:
                    next_layer.append(node.left)
                    next_layer.append(node.right)
            layer = next_layer
        # Remove NULLs from tail of lst.
        while lst[-1] == NULL:
            lst.pop()
        return SEPARATOR.join(lst)
    

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None
        lst = data.split(SEPARATOR)
        root = TreeNode(int(lst.pop(0)))
        layer: list[TreeNode] = [root]
        while layer:
            next_layer: list[TreeNode] = []
            for node in layer:
                item1 = NULL if not lst else lst.pop(0)
                item2 = NULL if not lst else lst.pop(0)
                node.left = None if item1 == NULL else TreeNode(int(item1))
                node.right = None if item2 == NULL else TreeNode(int(item2))
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            layer = next_layer
        return root
