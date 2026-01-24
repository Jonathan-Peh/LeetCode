class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for y in range(1,len(word2)+1):
            dp[y][0] = y
        for x in range(1,len(word1)+1):
            dp[0][x] = x
        
        for y in range(1,len(word2)+1):
            for x in range(1,len(word1)+1):
                dp[y][x] = min(dp[y-1][x]+1,dp[y][x-1]+1,dp[y-1][x-1]+(1 if word1[x-1] != word2[y-1] else 0))

        return dp[-1][-1]
