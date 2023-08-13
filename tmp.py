class Solution:
    def twoSum(self, nums, target):
        arr = []
        for i in nums:
            for j in nums:
                if i + j == target and i != j:
                    arr.append(i)
                    arr.append(j)
        return arr

solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))
