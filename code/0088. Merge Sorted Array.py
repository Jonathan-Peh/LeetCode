class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i_run = m+n-1
        i_1 = m-1
        i_2 = n-1

        while i_1 >= 0 and i_2 >= 0:
            first = nums1[i_1]
            second = nums2[i_2]
            if first > second:
                nums1[i_run] = first
                i_1 -= 1
            else:
                nums1[i_run] = second
                i_2 -= 1
            i_run -= 1

        while i_2 >= 0:
            nums1[i_run] = nums2[i_2]
            i_2 -= 1
            i_run -= 1
