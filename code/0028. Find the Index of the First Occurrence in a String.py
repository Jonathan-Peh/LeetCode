class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            matched = True
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    matched = False
                    break
            if matched:
                return i

        return -1
