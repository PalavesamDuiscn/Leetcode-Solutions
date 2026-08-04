class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        r=[]
        for i in range(len(nums)):
            count=0
            for ch in nums:
                if nums[i]>ch:
                    count+=1
            r.append(count)
        return r
        