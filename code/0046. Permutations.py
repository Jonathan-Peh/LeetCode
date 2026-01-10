class Solution(object):
    def permute(self, nums):
        permutations = []
        stack = [[[],nums]]
        while stack:
            node,unplaced = stack.pop()
            if not unplaced:
                permutations.append(node)
            for u in range(len(unplaced)):
                stack.append([node+[unplaced[u]],unplaced[:u]+unplaced[u+1:]])
        return permutations
