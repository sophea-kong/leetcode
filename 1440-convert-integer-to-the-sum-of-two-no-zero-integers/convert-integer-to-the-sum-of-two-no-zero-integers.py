class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        left,right = 0,n
        while(left<=right):
            if(left + right == n and "0" not in str(left) and "0" not in str(right)):
                return [left,right]
            else:
                left += 1
                right -= 1