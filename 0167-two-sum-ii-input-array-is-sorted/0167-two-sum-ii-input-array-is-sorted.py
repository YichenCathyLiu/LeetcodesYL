class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        diary = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in diary.keys():
                return [diary[diff],i+1]
            else:
                diary[numbers[i]] = i+1
        