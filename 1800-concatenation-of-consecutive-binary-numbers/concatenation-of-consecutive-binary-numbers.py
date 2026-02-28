class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        length = 0   # number of bits
        
        for i in range(1, n + 1):
            # check if i is power of 2
            if (i & (i - 1)) == 0:
                length += 1
            
            # shift left and add current number
            result = ((result << length) | i) % MOD
        
        return result
        