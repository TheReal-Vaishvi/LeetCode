class Solution(object):
    def myAtoi(self, s):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Check overflow before adding digit
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result