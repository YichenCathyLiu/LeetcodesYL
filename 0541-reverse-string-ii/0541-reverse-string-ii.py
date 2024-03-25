class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # 转换为列表，因为字符串在Python中是不可变的
        s = list(s)
        for i in range(0, len(s), 2*k):
            # 直接在这里反转每个需要反转的部分
            s[i:i+k] = reversed(s[i:i+k])
        # 将列表转换回字符串
        return ''.join(s)