class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
                continue
            if c == '[':
                stack.append(']')
                continue
            if c == '{':
                stack.append('}')
                continue


            if c == ')':
                if (len(stack) == 0) or stack[-1] != ')':
                    return False
                else:
                    stack.pop()
                    continue
            if c == ']':
                if (len(stack) == 0) or stack[-1] != ']':
                    return False
                else:
                    stack.pop()
                    continue
            if c == '}':
                if (len(stack) == 0) or (stack[-1] != '}'):
                    return False
                else:
                    stack.pop()
                    continue


        if len(stack) != 0:
            return False

        return True




# ========================================================
solution = Solution()
s = "([)]"
print solution.isValid(s)
