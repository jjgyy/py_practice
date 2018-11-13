class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            result.append(nums)
            return result

        visited = {}
        for index in range(len(nums)):
            if nums[index] in visited:
                continue

            visited[nums[index]] = True
            sons = self.permuteUnique(nums[:index] + nums[index+1:])
            for son in sons:
                son.append(nums[index])
                result.append(son)

        return result


# =================================================================================

solution = Solution()
nums = [1, 1, 2]
print solution.permuteUnique(nums)
