class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        substring = ""
        for c in s:
            if c not in substring:
                substring = substring + c
                if len(substring) > maxLength:
                    maxLength = len(substring)
            else:
                index = substring.index(c)
                substring = substring[index+1:] + c

        return maxLength
        # length = len(s)
        # if length == 1:
        #     return 1
        # dic = {}
        # maxLength = 0
        # substringLength = 0
        # index = 0
        # while index < length:
        #     if s[index] not in dic:
        #         dic[s[index]] = index
        #         substringLength += 1
        #     else:
        #         index = dic[s[index]]
        #         if substringLength > maxLength:
        #             maxLength = substringLength
        #         substringLength = 0
        #         dic = {}
        #     index += 1
        #
        # if substringLength > maxLength:
        #     maxLength = substringLength
        # return maxLength

# ==================================
solution = Solution()
s = " "
print solution.lengthOfLongestSubstring(s)