class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = str(x)
            x = x[::-1]
        else:
            x = str(x)
            x = x[1:]
            x = '-' + x[::-1]

        x = float(x)
        if (x < float(-2 << 30)) | (x >= float(2 << 30)):
            return 0
        x = int(x)
        return x


# ===================================================
solution = Solution()
x = 1563847412
print(float(2 << 30))
print solution.reverse(x)
