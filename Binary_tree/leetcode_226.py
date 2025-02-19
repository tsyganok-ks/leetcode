# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert the tree, and return its root
        :param root: Binary tree
        :return: root
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root