import sys

class Solution(object):
    list = []
    def generate(self, s, s1, s2):
        if s1 == '':
            self.list.append(s + s2)
        if s2 == '':
            self.list.append(s + s1)
        if s1 != '':
            self.generate(s+s1[0], s1[1:], s2)
        if s2 != '':
            self.generate(s+s2[0], s1, s2[1:])

    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
                continue
            if c == ')':
                if (len(stack) == 0) or stack[-1] != ')':
                    return False
                else:
                    stack.pop()
                    continue
        if len(stack) != 0:
            return False

        return True


line1 = sys.stdin.readline().strip()
s11 = str(line1)
line2 = sys.stdin.readline().strip()
s22 = str(line2)
solution = Solution()
solution.generate('', s11, s22)
pipeis = set(solution.list)
count = 0
for e in pipeis:
    if solution.isValid(e):
        count += 1
print count
