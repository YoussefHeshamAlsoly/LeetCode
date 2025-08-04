# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import log, ceil, floor
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def count_nodes(root):
            if not root:
                return 0
            return 1 + count_nodes(root.left) + count_nodes(root.right)

        length = count_nodes(root)
        # print(length)
        if length in [1, 2]:
            return length - 1
        elif log(length)/log(2) == int(log(length)/log(2)):
            return int(log(length)/log(2))
        else:
            return int(floor(2*( log (length) / log(2) ) - 1 ))