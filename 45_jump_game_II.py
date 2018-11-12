class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        level = 0
        current_max = 0
        next_max = 0
        i = 0

        if len(nums) == 1:
            return 0

        while current_max - i >= 0:
            level += 1
            while i <= current_max:
                next_max = max(i + nums[i], next_max)
                if next_max >= len(nums) - 1:
                    return level
                i += 1
            current_max = next_max

        return 0



# ============================================

solution = Solution()
nums = [2, 3, 1, 1, 4]
print solution.jump(nums)
