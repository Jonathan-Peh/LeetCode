from collections import deque

class Solution(object):
    def generateParenthesis(self, n):

        solution = []
        queue = deque([("",0,0)])

        while queue:
            x,lvl,opens = queue.popleft()
            if len(x) == 2*n:
                solution.append(x)
            if opens < n:
                queue.append((x+"(",lvl+1,opens+1))
            if lvl > 0:
                queue.append((x+")",lvl-1,opens))

        return solution
