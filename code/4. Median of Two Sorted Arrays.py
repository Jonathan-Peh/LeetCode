class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        total_length = len(nums1) + len(nums2)
        right = total_length//2 + 1
        left = right - (0 if total_length%2 else 1)
        val_left = None
        val_right = None

        i1 = 0
        i2 = 0
        length = 0
        while length < right:
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] >= nums2[i2]:
                    elem = nums2[i2]
                    i2 += 1
                else:
                    elem = nums1[i1]
                    i1 += 1
            elif i1 == len(nums1):
                elem = nums2[i2]
                i2 += 1
            elif i2 == len(nums2):
                elem = nums1[i1]
                i1 += 1
            length += 1

            if length == left:
                val_left = elem
            if length == right:
                val_right = elem
        return (val_left + val_right)/2.0
