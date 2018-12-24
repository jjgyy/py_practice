class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if (nums[left] <= target) and (target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if (nums[mid] < target) and (target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# ========================================================
solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print solution.search(nums, target)
