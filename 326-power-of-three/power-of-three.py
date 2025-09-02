class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(n>1 and n%3==0):
            n = n/3
        return (n == 1)
        # result = n
        # while(result>1 and result%3==0):
        #     result = result/3
        # return (result == 1)
        