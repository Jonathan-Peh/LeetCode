class Solution(object):
    def sortColors(self, nums):
        n = {0:0,1:0,2:0}
        for i in range(len(nums)):
            n[nums[i]] += 1
        for i in range(n[0]):
            nums[i] = 0
        for i in range(n[0],n[0]+n[1]):
            nums[i] = 1
        for i in range(n[0]+n[1],n[0]+n[1]+n[2]):
            nums[i] = 2
