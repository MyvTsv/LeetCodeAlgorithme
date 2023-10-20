from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (not (0 <= len(nums1) <= 1000) or not (0 <= len(nums2) <= 1000) or not (1 <= len(nums1) + len(nums2) <= 2000)):
            return False

        mergedArray = nums1 + nums2
        sortedArray = sorted(mergedArray)

        if len(sortedArray) % 2 == 0:
            medianIndex = ((len(sortedArray)) // 2) - 1
            return (sortedArray[medianIndex] + sortedArray[medianIndex + 1]) / 2
        else:
            medianIndex = (len(sortedArray)) // 2
            return sortedArray[medianIndex]


assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
