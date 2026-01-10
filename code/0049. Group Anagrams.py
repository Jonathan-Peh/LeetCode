class Solution(object):
    def groupAnagrams(self, strs):
        groups = dict()
        for s in strs:
            letters = tuple(sorted(str(s)))
            if letters in groups:
                groups[letters].append(s)
            else:
                groups[letters] = [s]
        
        return groups.values()
