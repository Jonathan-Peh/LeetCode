class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        start = 0
        bag = []
        for i in range(len(s)):
            elem = s[i]
            if elem not in bag:
                bag.append(elem)
            else:
                test_len = i - start
                longest = max(test_len,longest)
                while elem in bag:
                    start += 1
                    bag = bag[1:]
                bag.append(elem)

        test_len = len(s) - start
        longest = max(test_len,longest)

        return longest
