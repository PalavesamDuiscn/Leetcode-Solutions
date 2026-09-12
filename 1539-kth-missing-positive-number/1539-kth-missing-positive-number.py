class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        result=[]
        for i  in range(1,len(arr)+k+1):
                if i not in arr:
                    result.append(i)
                    
                
        return result[k-1]
