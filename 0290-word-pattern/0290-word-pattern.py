class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        freq1={}
        freq2={}

        s=s.split(" ")

        for i,j in zip(pattern,s):

            if i in freq1 and freq1[i]!=j:
                return False
            if j in freq2 and freq2[j]!=i:
                return False
            
            freq1[i]=j
            freq2[j]=i

            if len(pattern)!=len(s):
                return False

        return True
        