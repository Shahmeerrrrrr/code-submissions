class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                value = board[r][c]
                box_r = r // 3
                box_c = c // 3
                box = (box_r, box_c)
                row_key = ("row", r, value)
                col_key = ("col", c, value)
                box_key = ("box", box, value)
                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True


