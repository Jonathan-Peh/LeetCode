class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = None
        cur_sum = None
        for i in range(len(nums)):
            if cur_sum is None or nums[i] > cur_sum + nums[i] :
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if max_sum<cur_sum or max_sum is None:
                max_sum = cur_sum

        return max_sum
