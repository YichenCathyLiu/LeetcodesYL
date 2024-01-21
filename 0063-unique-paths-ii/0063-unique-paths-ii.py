class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == [[0]]:
            return 1

        M,N = len(obstacleGrid),len(obstacleGrid[0])
        print(M,N)
        dp = {(M-1,N-1):1} # dictionary: take down how many ways each node have
        
        def dfs(r,c):
            if r == M or c == N or obstacleGrid[r][c]: 
            # touch the boundery or meet an obstacle
                return 0
            elif (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = dfs(r+1,c)+dfs(r,c+1)
            return dp[(r,c)]

        return dfs(0,0)

