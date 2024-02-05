class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # double pointers
        slow = 0
        result = []
        for fast in range(len(nums)):
            if nums[fast]!= val:
                nums[slow] = nums[fast]
                slow = slow+1
        return len(nums[0:slow])