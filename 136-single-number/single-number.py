class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for num in nums:
            result= result^num #solved by sung XOR bcz it rearrage and it gives same element as 0 and different one fives as same ex. 5 ^ 5 = 0,0 ^ 7 = 7
        return result    
        