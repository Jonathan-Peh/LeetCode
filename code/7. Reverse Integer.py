class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        digits = []
        while x > 0:
            digit,x = x%10,x//10
            digits.append(str(digit))
        if x:
            digits.append(str(x))
        if not digits:
            return 0
        result = int("".join(digits)) * sign
        if result < -2**31 or result > 2**31-1:
            return 0
        return result
