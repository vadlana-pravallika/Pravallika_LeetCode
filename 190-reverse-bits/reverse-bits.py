class Solution(object):
    def reverseBits(self, n):
        result = 0
        
        for _ in range(32):      # process 32 bits
            result = (result << 1) | (n & 1)  # add last bit of n
            n >>= 1              # shift n right
        
        return result

        