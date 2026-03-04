class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
        # Count 1s in each row
        row_count = [sum(row) for row in mat]
        
        # Count 1s in each column
        col_count = [0] * n
        for i in range(m):
            for j in range(n):
                col_count[j] += mat[i][j]
        
        # Count special positions
        special = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1
        
        return special