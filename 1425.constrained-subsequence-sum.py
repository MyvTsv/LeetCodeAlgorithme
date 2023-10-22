from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        numsSize = len(nums)
        if k == 1:
            return max(nums)
        result: List[int] = [nums[0]]
        print(result)
        for indexI in range(0, numsSize):
            bestValue: int = nums[indexI]
            indexJ = indexI
            while (indexJ - indexI) < k and indexI < indexJ:
                if indexJ >= numsSize:
                    bestValue = None
                elif (bestValue < nums[indexJ]) and not (nums[indexJ] in result):
                    bestValue = nums[indexJ]

                indexJ += 1
            if bestValue != None:
                result.append(bestValue)
        print(result)
        return sum(result)

assert Solution().constrainedSubsetSum([10,2,-10,5,20], 2) == 37
assert Solution().constrainedSubsetSum([-1,-2,-3], 1) == -1
assert Solution().constrainedSubsetSum([10,-2,-10,-5,20], 2) == 23
assert Solution().constrainedSubsetSum([4681,6466,9411,-5130,6047], 3) == 26605