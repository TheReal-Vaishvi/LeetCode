class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow = 0
        goingDown = False

        for ch in s:
            rows[curRow] += ch

            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown

            curRow += 1 if goingDown else -1

        return "".join(rows)