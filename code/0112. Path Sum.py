# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root.val,root)] # sum till current node, current node
        while stack:
            sumTill, node = stack.pop()
            if sumTill == targetSum and not node.left and not node.right:
                return True
            else:
                next = node.left
                if next:
                    stack.append((sumTill+next.val,next))
                next = node.right
                if next:
                    stack.append((sumTill+next.val,next))
        return False
