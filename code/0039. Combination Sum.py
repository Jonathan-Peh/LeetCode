class Solution(object):
    def combinationSum(self, candidates, target):
        answer = set()
        stack = [[0]]
        while stack:
            node = stack.pop()
            for c in candidates:
                val = sum(node) + c
                if val == target:
                    answer.add(tuple(sorted(node[1:] + [c])))
                elif val < target:
                    stack.append(node + [c])

        return list(answer)
