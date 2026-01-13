class Solution(object):
    def climbStairs(self, n):
        def comb(n,k):
            def factorial(x):
                fact = 1
                for i in range(1,x+1):
                    fact *= i
                return fact
            return factorial(n)/factorial(k)/factorial(n-k)
        ways = 0
        n_1 = n
        n_2 = 0
        while n_1 >= 0:
            total_pos = n_1 + n_2
            ways += comb(total_pos,n_1)
            n_1 -= 2
            n_2 += 1
        return ways
