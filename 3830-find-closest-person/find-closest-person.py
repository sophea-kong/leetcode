class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        def abs(a):
            if(a<0):
                return -a
            else:
                return a

        if(abs(x-z)>abs(y-z)):
            return 2
        elif (abs(x-z)==abs(y-z)):
            return 0
        else:
            return 1