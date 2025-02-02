# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find max depth of binary tree
        :param root: binary tree
        :return: depth
        """
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        """
        Alternative version of finding max depth of binary tree
        :param root:
        :return:
        """
        if root:
            queue = deque()
            queue.append((root, 1))

            self.res = 0

            while queue:
                root, num = queue.popleft()

                if not root.left and not root.right:
                    self.res = max(self.res, num)

                if root.left:
                    queue.append((root.left, num + 1))
                if root.right:
                    queue.append((root.right, num + 1))

            return self.res
        else:
            return 0