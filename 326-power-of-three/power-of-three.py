class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = n
        while(result>1 and result%3==0):
            result = result/3
        return (result == 1)
        