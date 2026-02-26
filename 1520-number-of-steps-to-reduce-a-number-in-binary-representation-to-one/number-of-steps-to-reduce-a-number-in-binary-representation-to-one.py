class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0
        
        # Traverse from right to left (ignore the first bit for now)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # Odd → add 1 (causes carry), then divide
                steps += 2
                carry = 1
            else:
                # Even → just divide
                steps += 1
        
        # If there's a carry left at the most significant bit
        return steps + carry
        