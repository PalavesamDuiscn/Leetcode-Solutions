class Solution(object):
    def isPerfectSquare(self, num):

        for i in xrange(1,num+1):
            square=i*i
            
            if square==num:
                return True
            elif square>num:
                return False