class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        res=int("".join(map(str,digits)))
        v=res+1
        r=list(map(int,str(v)))

        return r