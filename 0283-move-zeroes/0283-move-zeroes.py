class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        i,j = 0,0 # two pointers
        while i<len(nums):
            if nums[i] == 0:
                i = i+1
            else:
                nums[j] = nums[i]
                j = j+1
                i = i+1
        while j <len(nums):
            nums[j] = 0
            j = j+1
        
        return nums