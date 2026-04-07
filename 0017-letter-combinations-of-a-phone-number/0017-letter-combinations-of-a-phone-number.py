class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
    
        # Mapping of digits to letters
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        # Backtracking function
        def backtrack(index, path):
            # If combination length equals digits length → store it
            if len(path) == len(digits):
                result.append(path)
                return
            
            # Get letters for current digit
            letters = phone[digits[index]]
            
            for char in letters:
                backtrack(index + 1, path + char)
        
        backtrack(0, "")
        return result