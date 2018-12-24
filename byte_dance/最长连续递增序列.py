class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        result = 1
        ptr = 0
        while ptr < len(nums) - 1:
            if nums[ptr] < nums[ptr+1]:
                count += 1
            else:
                result = max(result, count)
                count = 1
            ptr += 1

        result = max(result, count)
        return result


# ========================================================
solution = Solution()
nums = [1,3,5,4,7]
print solution.findLengthOfLCIS(nums)
