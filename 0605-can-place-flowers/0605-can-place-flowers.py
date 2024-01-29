class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if flowerbed ==[1] and n==0:
            return True
        if flowerbed ==[0] and n<=1:
            return True
        
        i = 0
        while i>=0 and i<=len(flowerbed)-1:
            if i == 0: # start
                if flowerbed[i] == 1:
                    i = i+2
                elif flowerbed[i+1] == 1:
                    i = i+2
                else:
                    flowerbed[i] = 1
                    i = i+2
                    n = n-1
            elif i == len(flowerbed)-1:
                if flowerbed[i] == 1:
                    i = i+2
                elif flowerbed[i-1] == 1:
                    i = i+2
                else:
                    flowerbed[i] = 1
                    i = i+2
                    n = n-1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] ==1
                i = i+2
                n = n-1
            else:
                i = i+1
        
        return True if n <= 0 else False