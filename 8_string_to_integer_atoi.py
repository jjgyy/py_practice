class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        spaceCount = 0
        for char in str:
            if char == ' ':
                spaceCount += 1
            else:
                break
        str = str[spaceCount:]

        if str == "":
            return 0

        if not ((str[0] >= '0') & (str[0] <= '9')) | (str[0] == '-') | (str[0] == '+'):
            return 0

        if (str[0] == '-'):
            str = str[1:]
            numCount = 0
            for char in str:
                if (char >= '0') & (char <= '9'):
                    numCount += 1
                else:
                    break
            if numCount == 0:
                return 0
            str = str[0:numCount]
            result = self.toInt(-long(str))
            return result

        if (str[0] == '+'):
            str = str[1:]

        numCount = 0
        for char in str:
            if (char >= '0') & (char <= '9'):
                numCount += 1
            else:
                break
        if numCount == 0:
            return 0
        str = str[0:numCount]
        result = self.toInt(long(str))
        return result



    def toInt(self, num):
        if num < -(2 << 30):
            return -(2 << 30)
        if num >= (2 << 30):
            return (2 << 30) - 1
        return num


# =====================================
solution = Solution()
str = "+111"
print solution.myAtoi(str)