class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        singles = set(nums)
        if len(singles) == len(nums):
            return False
        else:
            return True