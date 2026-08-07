class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:]=reversed(s)
        return s