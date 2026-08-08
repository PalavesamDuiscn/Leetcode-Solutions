class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            for ch in stones:
                if i==ch:
                    count+=1
                # else:
                #     count=0
        return count
