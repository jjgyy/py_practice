class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_scanner = 0
        p_scanner = 0

        while p_scanner < len(p):
            if p[p_scanner] == '*':
                if p_scanner == len(p) - 1:
                    return True
                while p[p_scanner+1] == '*':
                    p_scanner += 1
                    if p_scanner == len(p) - 1:
                        return True
                while not self.isMatch(s[s_scanner:], p[(p_scanner+1):]):
                    s_scanner += 1
                    if s_scanner >= len(s):
                        return False
                return True
            elif p[p_scanner] == '?':
                s_scanner += 1
                p_scanner += 1
                if s_scanner > len(s):
                    return False
            elif ('a' <= p[p_scanner]) & (p[p_scanner] <= 'z'):
                if s_scanner >= len(s):
                    return False
                if p[p_scanner] != s[s_scanner]:
                    return False
                s_scanner += 1
                p_scanner += 1

        if s_scanner != len(s):
            return False

        return True

# ===================================

solution = Solution()
s = "ho"
p = "ho**"
print solution.isMatch(s, p)
