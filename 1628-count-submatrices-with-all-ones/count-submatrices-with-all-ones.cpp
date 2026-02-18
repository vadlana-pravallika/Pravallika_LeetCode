class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        vector<vector<int>> prefixSum(n, vector<int>(m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                prefixSum[i][j] = mat[i][j];
                if (i) prefixSum[i][j] += prefixSum[i - 1][j];
                if (j) prefixSum[i][j] += prefixSum[i][j - 1];
                if (i && j) prefixSum[i][j] -= prefixSum[i - 1][j - 1];
            }
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                for (int u = i; u < n; ++u) {
                    for (int v = j; v < m; ++v) {
                        int curSum = prefixSum[u][v];
                        if (j) curSum -= prefixSum[u][j - 1];
                        if (i) curSum -= prefixSum[i - 1][v];
                        if (i && j) curSum += prefixSum[i - 1][j - 1];

                        if (curSum == (u - i + 1) * (v - j + 1)) ++ans;
                    }
                }
            }
        }

        return ans;
    }
};