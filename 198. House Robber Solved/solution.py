class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1=0
        prev2=0

        for money in nums:
            rob = prev2 +money
            skip=prev1

            current = max (rob,skip)

            prev2=prev1
            prev1=current
        return prev1    
        
