class Solution(object):
    def lengthOfLastWord(self, s):
        last = s.split()[-1]
        return len(last)
