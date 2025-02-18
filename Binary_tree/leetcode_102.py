from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.answ = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return the level order traversal of its nodes' values
        :param root: binary tree
        :return: list of lists
        """
        if root:
            queue = deque()
            queue.append((root, 0))

            while queue:
                root, lvl = queue.popleft()

                if len(self.answ) <= lvl:
                    self.answ.append([root.val])
                else:
                    self.answ[lvl].append(root.val)

                if root.left:
                    queue.append((root.left, lvl + 1))

                if root.right:
                    queue.append((root.right, lvl + 1))

        return self.answ
