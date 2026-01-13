class Solution(object):
    def mySqrt(self, x):
        base = 0
        while base * base <= x:
            base += 1
        return base - 1
