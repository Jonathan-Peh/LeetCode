class Solution(object):
    def permuteUnique(self, nums):
        permutations = set()
        stack = [[[],nums]]
        while stack:
            node,unplaced = stack.pop()
            if not unplaced:
                permutations.add(tuple(node))
            for u in range(len(unplaced)):
                stack.append([node+[unplaced[u]],unplaced[:u]+unplaced[u+1:]])
        return list(permutations)
