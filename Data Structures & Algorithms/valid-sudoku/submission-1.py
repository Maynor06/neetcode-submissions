class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                if (num in rows[r]) or (num in columns[c]) or (num in squares[r // 3][c // 3]):
                    return False
                
                columns[c].add(num)
                rows[r].add(num)
                squares[r // 3][c // 3].add(num)
        return True
