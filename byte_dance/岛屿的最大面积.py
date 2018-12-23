class Solution(object):
    grid = []
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1:
                    tmp = self.findIsland(i, j)
                    maxArea = max(tmp, maxArea)

        return maxArea

    def findIsland(self, i, j):
        sum = 0
        self.grid[i][j] = 0
        sum += 1
        if (i < len(self.grid) - 1) and (self.grid[i+1][j] == 1):
            sum += self.findIsland(i+1, j)
        if (i > 0) and (self.grid[i-1][j] == 1):
            sum += self.findIsland(i-1, j)
        if (j < len(self.grid[i]) - 1) and (self.grid[i][j+1] == 1):
            sum += self.findIsland(i, j+1)
        if (j > 0) and (self.grid[i][j-1] == 1):
            sum += self.findIsland(i, j-1)

        return sum

# ========================================================
solution = Solution()
grid = \
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print solution.maxAreaOfIsland(grid)
