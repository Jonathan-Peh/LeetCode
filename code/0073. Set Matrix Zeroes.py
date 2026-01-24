class Solution(object):
    def setZeroes(self, matrix):
        '''list_x = set()
        list_y = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == 0:
                    list_x.add(x)
                    list_y.add(y)
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if y in list_y or x in list_x:
                    matrix[y][x] = 0'''

        # constant space version
        first_row_0 = False
        first_col_0 = False
        m = len(matrix)
        n = len(matrix[0])
        for x in range(n):
            if matrix[0][x] == 0:
                first_row_0 = True
                break
        for y in range(m):
            if matrix[y][0] == 0:
                first_col_0 = True
                break
        for y in range(1,m):
            for x in range(1,n):
                if matrix[y][x] == 0:
                    matrix[0][x] = 0
                    matrix[y][0] = 0
        for x in range(1,n):
            if matrix[0][x] == 0:
                for y in range(1,m):
                    matrix[y][x] = 0
        for y in range(1,m):
            if matrix[y][0] == 0:
                for x in range(1,n):
                    matrix[y][x] = 0
        if first_row_0:
            for x in range(n):
                matrix[0][x] = 0
        if first_col_0:
            for y in range(m):
                matrix[y][0] = 0
