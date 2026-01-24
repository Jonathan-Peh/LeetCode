class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]

        low = 0
        high = len(nums)
        found = False

        while high > low:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid
            else:
                found = True
                i_left = mid
                high = mid

        if not found:
            return [-1,-1]

        low = i_left
        high = len(nums)
        while high > low:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid
            else:
                found = True
                i_right = mid
                low = mid+1
        return [i_left,i_right]
