class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_length = len(s)
        max_length = 0
        longest_palindrome = ""
        ptrA = 0
        ptrB = s_length

        while (ptrB - ptrA) > max_length:
            while (ptrB - ptrA) > max_length:
                temp = s[ptrA:ptrB]
                if temp == temp[::-1]:
                    longest_palindrome = temp
                    max_length = ptrB - ptrA
                    break
                ptrB -= 1
            ptrA += 1
            ptrB = s_length

        return longest_palindrome



# ==========================================
solution = Solution()
s = "cabac"
print solution.longestPalindrome(s)
