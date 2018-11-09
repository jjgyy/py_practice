class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2 + n%2):
            for j in range(n/2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        print(matrix)


# ==================================================================

matrix1 = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
    [13,14,15,16]
]
matrix2 = [
    [1,2],
    [3,4]
]
solution = Solution()
solution.rotate(matrix2)
