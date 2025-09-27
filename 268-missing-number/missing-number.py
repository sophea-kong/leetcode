class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_num = set(range(0,len(nums)+1))
        for i in nums:
            if i in all_num:
                all_num.remove(i)
        return all_num.pop()