class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if val in rows[row]:
                    return False
                else:
                    rows[row].add(val)
                
                if val in cols[col]:
                    return False
                else:
                    cols[col].add(val)
                if val in grids[row//3][col//3]:
                    return False
                else:
                    grids[row//3][col//3].add(val)
                
        return True
