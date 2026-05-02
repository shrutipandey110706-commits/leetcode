class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len (nums) 
        total_subset=1<<n # menas 2^n ,here 3 so 2^3=8
        result=[]
        for num in range (0,total_subset):
            lst =[]
            for i in range (0,n):
                if num & (1<<i) !=0: # whether the number is set or not
                    lst.append(nums[i])
            result.append(lst)
        return result            