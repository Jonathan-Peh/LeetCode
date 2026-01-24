class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def nextRow(row):
            nxtrw = [1]
            for i in range(len(row)):
                if i == len(row)-1:
                    nxtrw.append(1)
                else:
                    nxtrw.append(row[i]+row[i+1])
            return nxtrw

        row = [1]
        for _ in range(rowIndex):
            row = nextRow(row)
        
        return row
