class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        # Create 2D DP array
        dp = [[0.0] * 101 for _ in range(101)]
        
        dp[0][0] = poured
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                if dp[row][col] > 1:
                    excess = (dp[row][col] - 1) / 2.0
                    dp[row + 1][col] += excess
                    dp[row + 1][col + 1] += excess
                    dp[row][col] = 1  # cap at full
        
        return min(1, dp[query_row][query_glass])

        