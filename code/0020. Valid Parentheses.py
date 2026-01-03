class Solution(object):
    def isValid(self, s):
        opening = {")":"(","}":"{","]":"["}
        stack = []
        for i in range(len(s)):
            sym = s[i]
            if sym in opening:
                if stack and stack[-1] == opening[sym]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        if not stack:
            return True
        else:
            return False
