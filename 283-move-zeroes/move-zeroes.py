class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range (len(nums)):
            if nums[i]!=0: #[0,1,0,3,12] → [1,0,0,3,12] & ,[1,0,0,3,12]→[1,3,0,0,12]
                nums[j],nums[i]=nums[i],nums[j]
                j+=1