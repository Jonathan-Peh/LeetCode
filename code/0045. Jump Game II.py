class Solution(object):
    def jump(self, nums):
        mins = {0:0}
        for i in range(1,len(nums)):
            for j in range(i):
                distance = i-j
                if distance <= nums[j] and (i not in mins or mins[j]+1<mins[i]):
                    mins[i] = mins[j] + 1

        return mins[len(nums)-1]
