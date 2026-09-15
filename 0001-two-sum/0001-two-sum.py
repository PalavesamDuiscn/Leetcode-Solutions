class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in nums:
                j = nums.index(needed)

                if i != j:
                    return [i, j]