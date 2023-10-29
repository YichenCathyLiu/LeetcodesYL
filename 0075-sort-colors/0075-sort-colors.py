class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = [0]*nums.count(0)
        one = [1]*nums.count(1)
        two = [2]*nums.count(2)
        
        nums[:] = zero+one+two
        
        
        
        
        