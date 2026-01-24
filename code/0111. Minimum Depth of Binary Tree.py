class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        min_depth = 10**5
        stack = [(root,1)]
        while stack:
            node,depth = stack.pop()
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
            if not (node.left or node.right):
                min_depth = min(min_depth,depth)
        return min_depth
