class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        t=""

        for i in s:
            if i.isalnum():
                t+=i
        
        right=len(t)-1
        left=0
        
        while left<right:
            
            if t[left]!=t[right]:
                return False

            left+=1
            right-=1
            
        return True

        