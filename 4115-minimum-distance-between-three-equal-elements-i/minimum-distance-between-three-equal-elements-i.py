class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        # Group indices by value
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        # Check each group
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # Sliding window of size 3
            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i + 2]
                
                # distance = 2 * (max_index - min_index)
                ans = min(ans, 2 * (right - left))
        
        return ans if ans != float('inf') else -1
        