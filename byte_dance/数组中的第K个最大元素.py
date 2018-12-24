class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) - k]

# ========================================================
solution = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print solution.findKthLargest(nums, k)
