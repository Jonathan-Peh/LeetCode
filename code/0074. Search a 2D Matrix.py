class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n_row = len(matrix)
        n_col = len(matrix[0])
        low = 0
        high = n_row*n_col
        while high > low:
            mid = (low+high)//2
            y = mid//n_col
            x = mid%n_col
            val = matrix[y][x]
            if target < val:
                high = mid
            elif target > val:
                low = mid + 1
            else:
                return True
        return False
