class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        
        arr_sum = 0
        for num in nums:
            arr_sum += num
        
        return total - arr_sum