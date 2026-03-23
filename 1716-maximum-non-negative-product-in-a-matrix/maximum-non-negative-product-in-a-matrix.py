class Solution(object):
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # dp arrays
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        # initialize
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # first column
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        
        # first row
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
        
        # fill rest
        for i in range(1, m):
            for j in range(1, n):
                x = grid[i][j]
                
                candidates = [
                    x * max_dp[i-1][j],
                    x * min_dp[i-1][j],
                    x * max_dp[i][j-1],
                    x * min_dp[i][j-1]
                ]
                
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
        
        result = max_dp[m-1][n-1]
        
        if result < 0:
            return -1
        
        return result % (10**9 + 7)
        