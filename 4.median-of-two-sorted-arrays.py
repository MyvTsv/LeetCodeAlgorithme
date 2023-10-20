from typing import List

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if(not (0 <= len(nums1) <= 1000) or not (0 <= len(nums2) <= 1000) or not(1 <= len(nums1) + len(nums2) <= 2000)): return False
#         mergeArray = nums1 + nums2
#         for i in range(0, len(mergeArray)):
#             for j in range(i, len(mergeArray)):
#                 if mergeArray[i] > mergeArray[j]:
#                     temp = mergeArray[i]
#                     mergeArray[i] = mergeArray[j]
#                     mergeArray[j] = temp
#         if len(mergeArray) % 2 == 0:
#             medianIndex = int((len(mergeArray)) / 2) - 1
#             return (mergeArray[medianIndex] + mergeArray[medianIndex + 1]) / 2
#         else:
#             medianIndex = int((len(mergeArray)) / 2)
#             return mergeArray[medianIndex]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(not (0 <= len(nums1) <= 1000) or not (0 <= len(nums2) <= 1000) or not(1 <= len(nums1) + len(nums2) <= 2000)): return False

        def mergeSort(array: List[int]) -> List[int]:
            print('array : ', array)
            arraySize = len(array)
            if(arraySize == 1): return array
            mergeArray: List[int] = []
            midIndex = arraySize // 2
            leftArray = mergeSort(array[:midIndex])
            rightArray = mergeSort(array[midIndex:])
            leftIndex = 0
            rightIndex = 0
            while len(leftArray) < leftIndex and len(rightArray) < rightIndex:
                if leftArray[leftIndex] >= rightArray[rightIndex]:
                    mergeArray.append(rightArray[rightIndex])
                    rightIndex += 1
                else:
                    mergeArray.append(leftArray[leftIndex])
                    leftIndex += 1
            if len(leftArray) == leftIndex:
                mergeArray + rightArray
            else:
                mergeArray + leftArray
            return mergeArray
            

        sortedArray = mergeSort(nums1 + nums2)

        if len(sortedArray) % 2 == 0:
            medianIndex = int((len(sortedArray)) / 2) - 1
            return (sortedArray[medianIndex] + sortedArray[medianIndex + 1]) / 2
        else:
            medianIndex = int((len(sortedArray)) / 2)
            return sortedArray[medianIndex]


assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
