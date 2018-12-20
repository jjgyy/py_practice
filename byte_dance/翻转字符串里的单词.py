class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = s.split(' ')
        array.reverse()
        array = [elem for elem in array if elem != '']
        result = ' '.join(array)
        return result


# ========================================================
solution = Solution()
s = "    "
print "'" + solution.reverseWords(s) + "'"
