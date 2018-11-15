class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        indexA = 0
        indexB = len(height) - 1
        result = 0
        while indexA < indexB:
            l = height[indexA]
            r = height[indexB]
            if l >= r:
                result = max(result, r*(indexB-indexA))
                indexB -= 1
            else:
                result = max(result, l*(indexB-indexA))
                indexA += 1
        return result

# ===========================================
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print solution.maxArea(height)
