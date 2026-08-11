class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        r=[]
        for i in accounts:
            sum=0
            for j in i:
                sum+=j
                r.append(sum)
        return max(r)

        