class Solution(object):
    def romanToInt(self, s):
        dictionary = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        lastelem = 0
        total = 0
        for i in range(len(s)-1,-1,-1):
            if dictionary[s[i]] >= lastelem:
                lastelem = dictionary[s[i]] 
                total = total + lastelem
            elif dictionary[s[i]] < lastelem:
                lastelem = dictionary[s[i]]
                total = total - lastelem
        return(total)
