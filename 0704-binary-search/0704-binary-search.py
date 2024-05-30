class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 注意这个nums数组已经是没有重复数字而且升序的

        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = l+((r-l)//2)  # use // to prevent leaking
            if nums[m]<target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        
        return -1
            
            