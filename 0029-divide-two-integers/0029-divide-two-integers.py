class Solution(object):
    def divide(self, dividend, divisor):
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # Subtract divisor multiples using bit shifting
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double temp until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        return sign * quotient
        