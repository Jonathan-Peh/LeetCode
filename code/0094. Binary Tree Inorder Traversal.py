# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        Traversal = []
        queue = deque([(root,False)])
        while queue:
            node,flag = queue.popleft()
            if not flag:
                left, right = node.left, node.right
                if right:
                    queue.appendleft((right,False))
                queue.appendleft((node,True))
                if left:
                    queue.appendleft((left,False))
            else:
                Traversal.append(node.val)

        return Traversal
