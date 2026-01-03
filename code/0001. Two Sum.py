class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in index:
                index[num].append(i)
            else:
                index[num] = [i]

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in index:
                js = index[complement]
                for j in js:
                    if j != i:
                        return [j,i]
