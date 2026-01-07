class Solution(object):
    def isValidSudoku(self, board):
        for row in range(9):
            collection = []
            for col in range(9):
                if board[row][col] in collection:
                    return False
                elif board[row][col] != ".":
                    collection.append(board[row][col])

        for col in range(9):
            collection = []
            for row in range(9):
                if board[row][col] in collection:
                    return False
                elif board[row][col] != ".":
                    collection.append(board[row][col])
            
        for subbox_y in range(3):
            for subbox_x in range(3):
                collection = []
                for row in range(3):
                    for col in range(3):
                        if board[3*subbox_y + row][3*subbox_x + col] in collection:
                            return False
                        elif board[3*subbox_y + row][3*subbox_x + col] != ".":
                            collection.append(board[3*subbox_y + row][3*subbox_x + col])

        return True
