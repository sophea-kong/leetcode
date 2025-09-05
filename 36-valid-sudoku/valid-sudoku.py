class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #row
        for i in range(9):
            temp_set = set()
            for j in range(9):
                if (board[i][j] == "."):
                    continue
                elif (not board[i][j] in temp_set):
                    temp_set.add(board[i][j])
                else :
                    return False
        #col
        for i in range(9):
            temp_set = set()
            for j in range(9):
                if (board[j][i] == "."):
                    continue
                elif (not board[j][i] in temp_set):
                    temp_set.add(board[j][i])
                else :
                    return False
        #sub-box
        for start_row in range(0,9,3):
            for start_col in range(0,9,3):
                temp_set = set()
                for i in range(start_row,start_row+3):
                    for j in range(start_col,start_col+3):
                        if (board[i][j] == "."):
                            continue
                        elif (not (board[i][j] in temp_set)):
                            temp_set.add(board[i][j])
                        else:
                            return False
        return True