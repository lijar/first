class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], i]
            index[x] = i
solution = Solution()
print solution.twoSum([2,7,11,15], 9)
