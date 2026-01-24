class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def nextRow(row):
            nxtrw = [1]
            for i in range(len(row)):
                if i == len(row)-1:
                    nxtrw.append(1)
                else:
                    nxtrw.append(row[i]+row[i+1])
            return nxtrw

        rows = [[1]]
        for i in range(numRows-1):
            rows.append(nextRow(rows[-1]))

        return rows
