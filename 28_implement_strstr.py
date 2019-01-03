class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        result = -1

        try:
            result = haystack.index(needle)
        except ValueError:
            result = -1

        return result


# ========================================================
solution = Solution()
haystack = "hello"
needle = "elle"
print solution.strStr(haystack, needle)
