class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)//2):
            if x[i] == x[-(i+1)]:
                continue
            else:
                return(False)
        return(True)
