class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        longest_palindrome = ""
        ptrA = 0
        ptrB = len(s) - 1
        while True:
            ptrB = len(s) - 1
            if (ptrB - ptrA + 1) <= max_length:
                break
            while True:
                if (ptrB - ptrA + 1) <= max_length:
                    break
                if self.is_palindromic(s[ptrA:ptrB+1]):
                    longest_palindrome = s[ptrA:ptrB+1]
                    max_length = ptrB - ptrA + 1
                    break
                ptrB -= 1
            ptrA += 1

        return longest_palindrome

    def is_palindromic(self, s):
        if s == s[::-1]:
            return True
        return False


# ==========================================
solution = Solution()
s = "aba"
print solution.longestPalindrome(s)
