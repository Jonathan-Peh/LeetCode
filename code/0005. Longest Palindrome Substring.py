def longestFromNucleus(s,left,right):
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            return s[left+1:right]
    return s[left+1:right]

class Solution(object):

    def longestPalindrome(self, s):
        longest = (0,None)
        for i in range(len(s)):
            if i+1 < len(s) and s[i] == s[i+1]:
                left,right = i,i+1
                substring = longestFromNucleus(s,left,right)
                length = len(substring)
                if longest[0] < length:
                    longest = (length,substring)
            left = i - 1
            right = i + 1
            substring = longestFromNucleus(s,left,right)
            length = len(substring)
            if longest[0] < length:
                longest = (length,substring)
        return longest[1]
