class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        a=nums[:n]
        b=nums[n:]
        result=[]

        for i,j in zip(a,b):
            result.append(i)
            result.append(j)
        return result 

        