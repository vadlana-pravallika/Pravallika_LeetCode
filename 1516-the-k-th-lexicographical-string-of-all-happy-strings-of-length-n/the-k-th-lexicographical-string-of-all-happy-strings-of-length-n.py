class Solution(object):
    def getHappyString(self, n, k):
        res = []
        chars = ['a', 'b', 'c']

        def backtrack(path):
            if len(res) >= k:
                return
            
            if len(path) == n:
                res.append(path)
                return
            
            for c in chars:
                if not path or path[-1] != c:
                    backtrack(path + c)

        backtrack("")
        
        return res[k-1] if k <= len(res) else ""