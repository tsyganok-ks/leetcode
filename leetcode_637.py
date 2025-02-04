from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Calculate the average value of the nodes on each level in the form of an array
        :param root: tree
        :return: list of averages
        """
        if root:
            queue = deque()
            queue.append((root, 0))
            self.averages = []

            while queue:
                root, lvl = queue.popleft()

                if len(self.averages) <= lvl:
                    self.averages.append([root.val])
                else:
                    self.averages[lvl].append(root.val)

                if root.left:
                    queue.append((root.left, lvl + 1))

                if root.right:
                    queue.append((root.right, lvl + 1))

        return [sum(lvl)/len(lvl) for lvl in self.averages]
