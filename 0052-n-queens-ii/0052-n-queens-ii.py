class Solution(object):
    def totalNQueens(self, n):
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        count = [0]  # using list to make it mutable

        def backtrack(row):
            if row == n:
                count[0] += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # backtrack
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return count[0]