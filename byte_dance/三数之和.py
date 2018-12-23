class Solution(object):
    nums = []
    result = []
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        self.nums = nums
        length = len(nums)
        index = 0
        while index <= length - 3:
            self.twoSum(-self.nums[index], index+1, length-1)
            index += 1
            while (index <= length - 3) & (self.nums[index] == self.nums[index-1]):
                index += 1

        return self.result

    def twoSum(self, sum, begin, end):
        while begin < end:
            twoSum = self.nums[begin] + self.nums[end]
            if twoSum == sum:
                self.result.append([-sum, self.nums[begin], self.nums[end]])
                while (begin < end - 1) & (self.nums[begin + 1] == self.nums[begin]):
                    begin += 1
                while (begin < end - 1) & (self.nums[end - 1] == self.nums[end]):
                    end -= 1
                begin += 1
                end -= 1
            else:
                if twoSum < sum:
                    begin += 1
                else:
                    end -= 1




# ========================================================
solution = Solution()
nums = [0,0,0]
print solution.threeSum(nums)
