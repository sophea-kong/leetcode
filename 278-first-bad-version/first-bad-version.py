# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 0,n
        while(left<right):
            if(isBadVersion((left+right)//2)):
                right = (left+right)//2
            else:
                left = (left+right)//2 +1
        return left