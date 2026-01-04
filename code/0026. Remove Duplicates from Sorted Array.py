class Solution(object):
    def removeDuplicates(self, nums):
        last_elem = nums[0]
        write_i = 1

        for read_i in range(1,len(nums)):
            elem = nums[read_i]
            if elem != last_elem:
                nums[write_i] = elem
                last_elem = elem
                write_i += 1

        return write_i
