class Solution(object):
    def printNumbers(self, lower, upper):
        '''
        use 'while' and 'break' to print all integer between lower and upper
        for example:
        lower = 0, upper = 5
        you should print:
        0
        1
        2
        3
        4
        5

        tips: Do not use 'for'!, this is a 'while' practice

        'break' is optional, if you use 'while True:' , 'break' may help you to quit the loop

        :param lower:
        :param upper:
        :return: None(no need to return)
        '''



# ========================================================
solution = Solution()

lower1 = 1
upper1 = 10

lower2 = -5
upper2 = 12

solution.printNumbers(lower1, upper1)
solution.printNumbers(lower2, upper2)
