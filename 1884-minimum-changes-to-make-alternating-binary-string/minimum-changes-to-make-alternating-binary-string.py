class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        start0 = 0
        start1 = 0
        
        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                start0 += 1
            if s[i] != ('1' if i % 2 == 0 else '0'):
                start1 += 1
        
        return min(start0, start1)