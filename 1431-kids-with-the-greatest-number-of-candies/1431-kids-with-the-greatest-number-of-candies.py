class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        r=[]
        s=max(candies)
        for i in candies:
            if i + extraCandies>=s:
                r.append(True)
            else:
                r.append(False)
        return r


        