class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            result.append(nums)
            return result
        for index in range(len(nums)):
            sons = self.permute(nums[:index] + nums[index+1:])
            for son in sons:
                son.append(nums[index])
                result.append(son)

        return result


# =================================================================================

solution = Solution()
nums = [1, 2, 3, 4]
print solution.permute(nums)
