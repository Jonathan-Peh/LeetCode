class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
        for y in range(1,len(s2)+1):
            dp[y][0] = dp[y-1][0] + ord(s2[y-1])
        for x in range(1,len(s1)+1):
            dp[0][x] = dp[0][x-1] + ord(s1[x-1])
        for y in range(1,len(s2)+1):
            for x in range(1,len(s1)+1):
                if s2[y-1] != s1[x-1]:
                    dp[y][x] = min(dp[y-1][x]+ord(s2[y-1]),dp[y][x-1]+ord(s1[x-1]))
                else:
                    dp[y][x] = dp[y-1][x-1]

        return dp[-1][-1]
