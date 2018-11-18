class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum



# ==================================
solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s_nums = [-1]
print solution.maxSubArray(s_nums)
