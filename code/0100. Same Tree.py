# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue1 = deque([(p,False)])
        queue2 = deque([(q,False)])
        a,b = None,None
        while queue1 and queue2:

            node,flag = queue1.popleft()
            if not flag:
                left, right = node.left, node.right
                if right:
                    queue1.appendleft((right,False))
                queue1.appendleft((node,True))
                if left:
                    queue1.appendleft((left,False))
            else:
                a = node.val

            node,flag = queue2.popleft()
            if not flag:
                left, right = node.left, node.right
                if right:
                    queue2.appendleft((right,False))
                queue2.appendleft((node,True))
                if left:
                    queue2.appendleft((left,False))
            else:
                b = node.val

            if a != b:
                return False

        return not queue1 and not queue2
