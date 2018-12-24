class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result = 1
        hashMap = {}
        for num in nums:
            hashMap[num] = True

        for num in hashMap:
            hashMap[num] = False
            left = num - 1
            right = num + 1
            while (left in hashMap) and (hashMap[left]):
                hashMap[left] = False
                left -= 1
            while (right in hashMap) and (hashMap[right]):
                hashMap[right] = False
                right += 1
            tmp = right - left - 1
            result = max(tmp, result)

        return result

# ========================================================
solution = Solution()
nums = [100, 4, 200, 1, 3, 2, 5]
print solution.longestConsecutive(nums)
