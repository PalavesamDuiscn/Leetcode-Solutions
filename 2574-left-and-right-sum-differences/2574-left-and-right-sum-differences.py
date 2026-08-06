class Solution(object):
    def leftRightDifference(self, nums):
        total_sum = 0
        left_sum = 0
        answer = []

        # First pass: Calculate the total sum
        for current in nums:
            total_sum += current

        # Second pass: Calculate the answer
        for current in nums:
            right_sum = total_sum - left_sum - current
            ans = abs(left_sum - right_sum)
            answer.append(ans)
            left_sum += current

        return answer