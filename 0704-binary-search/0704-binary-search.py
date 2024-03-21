class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 注意这个nums数组已经是没有重复数字而且升序的

        left = 0
        right = len(nums)-1

        while (left<=right):
            middle = left+(right-left)//2 # 整数除法自动去除小数部分
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle # found it!

        return -1 # 没找到