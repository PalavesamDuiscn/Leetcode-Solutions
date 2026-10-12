class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        freq={}
        res=[]
        r=0

        for i in nums:
            freq[i]=freq.get(i,0)+1

        for i in freq.values():
            res.append(i)
        r=max(res)

        for i in freq:
            if freq[i]==r:
                return i
        
        