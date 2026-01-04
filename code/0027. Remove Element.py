class Solution(object):
    def removeElement(self, nums, val):
        write_i = 0

        for read_i in range(len(nums)):
            elem = nums[read_i]
            if elem != val:
                nums[write_i] = elem
                write_i += 1

        return write_i
