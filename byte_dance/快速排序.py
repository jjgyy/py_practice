class Solution(object):
    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums
        tmp = nums[len(nums)]
        left = []
        right = []
        for num in nums[1:]:
            if num <= tmp:
                left.append(num)
            else:
                right.append(num)
        left = self.quickSort(left)
        right = self.quickSort(right)
        return left + [tmp] + right





# ========================================================
solution = Solution()
nums = [2,0,1,9,2,3,7]
print solution.quickSort(nums)
