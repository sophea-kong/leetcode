class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        squared = list()
        while(l<=r):
            if abs(nums[l]) > abs(nums[r]):
                squared.append(nums[l]**2)
                l+=1
            else:
                squared.append(nums[r]**2)
                r-=1
        return squared[::-1]
        