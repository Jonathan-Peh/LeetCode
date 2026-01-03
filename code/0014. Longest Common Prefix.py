class Solution(object):
    def longestCommonPrefix(self, strs):
        pre = ""
        short = None
        for s in strs:
            len_s = len(s)
            if len_s == 0:
                return ""
            if not short or len_s < short:
                short = len_s
        for i in range(short):
            ref = strs[0][i]
            matched = True
            for j in range(1,len(strs)):
                if strs[j][i] != ref:
                    matched = False
                    break
            if matched:
                pre = pre + ref
            else:
                break
        return pre
