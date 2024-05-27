class Solution(object):
    def productExceptSelf(self, nums):

        # 初始化结果数组，每个元素初始值为1
        res = [1] * (len(nums))

        # 第一遍遍历：计算每个元素的前缀乘积
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        # 初始化后缀乘积变量
        postfix = 1
        
        # 第二遍遍历：计算每个元素的后缀乘积，并与前缀乘积相乘
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res