class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        freq1 = {}
        freq2 = {}

        for i, j in zip(s, t):

            if i in freq1 and freq1[i] != j:
                return False

            if j in freq2 and freq2[j] != i:
                return False

            freq1[i] = j
            freq2[j] = i

        return True