class Solution(object):
    def findKthBit(self, n, k):
        # Base case
        if n == 1:
            return "0"
        
        mid = 2 ** (n - 1)
        
        # If k is the middle element
        if k == mid:
            return "1"
        
        # If k is in the left half
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        # If k is in the right half
        # Mirror index and invert result
        mirror = 2 ** n - k
        bit = self.findKthBit(n - 1, mirror)
        
        return "1" if bit == "0" else "0"