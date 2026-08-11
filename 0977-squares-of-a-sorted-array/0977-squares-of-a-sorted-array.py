class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        r=[]
        for i in nums:
            r.append(pow(i,2))
            r.sort()
        return r
            
        