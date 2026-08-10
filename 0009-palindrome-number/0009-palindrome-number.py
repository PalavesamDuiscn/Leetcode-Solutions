class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=x
        r=0
        while x>0:
            r=r*10+x%10
            x=x//10
        if r==i:
            return True
        else:
            return False

        