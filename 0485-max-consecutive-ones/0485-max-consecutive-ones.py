class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        max_count = 0

        for i in nums:
            if i == 1:
                a += 1
                max_count = max(max_count, a)
            else:
                a = 0

        return max_count