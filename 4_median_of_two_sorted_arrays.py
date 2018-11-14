class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge_nums = []
        index1 = 0
        index2 = 0
        length1 = len(nums1)
        length2 = len(nums2)
        while True:
            if index1 >= length1:
                if index2 < length2:
                    merge_nums += nums2[index2:]
                break
            if index2 >= length2:
                if index1 < length1:
                    merge_nums += nums1[index1:]
                break

            if nums1[index1] <= nums2[index2]:
                merge_nums.append(nums1[index1])
                index1 += 1
            else:
                merge_nums.append(nums2[index2])
                index2 += 1

        if (length1 + length2) % 2 == 1:
            return float(merge_nums[(length1 + length2 - 1) / 2])
        else:
            return ( float(merge_nums[(length1 + length2)/2 - 1]) + float(merge_nums[(length1 + length2)/2]) ) / 2



# ==========================================
solution = Solution()
nums1 = [1, 3]
nums2 = [2, 4]
print solution.findMedianSortedArrays(nums1, nums2)
