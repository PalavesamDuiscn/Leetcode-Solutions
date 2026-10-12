class Solution:
    def scoreOfString(self, s: str) -> int:

        r=0
        h=list(s)
        m=0
        for i in range(len(h)-1):
            a=ord(h[i])
            b=ord(h[i+1])

            r=abs(a-b) 
            m+=r
        return m

        