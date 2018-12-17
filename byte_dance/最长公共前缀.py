class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        minLength = len(strs[0])
        minLengthWord = strs[0]
        for s in strs:
            if minLength > len(s):
                minLength = len(s)
                minLengthWord = s

        commonPrefix = ""
        shouldEnd = False
        for index in range(minLength):
            commonChar = minLengthWord[index]
            for s in strs:
                if s[index] != commonChar:
                    shouldEnd = True
                    break

            if shouldEnd:
                break
            commonPrefix = commonPrefix + commonChar

        return commonPrefix

# ====================================================

solution = Solution()
strs = ["flower", "flow", "flight"]
print solution.longestCommonPrefix(strs)