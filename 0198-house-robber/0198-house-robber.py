class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums)<=2:
            return max(nums)

        dp = [0] * (len(nums)) # 建立dp数组

        # dp[i] 记录的是到第 i 个房子时，能抢劫到的最大金额
        dp[0] = nums[0]  # 如果只抢第一个房子
        dp[1] = max(nums[0], nums[1])  # 抢第一个或第二个房子，取最大值

        # 从第 3 个房子开始，计算最大金额
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        # 返回最后一个房子的最大抢劫金额
        return dp[-1]