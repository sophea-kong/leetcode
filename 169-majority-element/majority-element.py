class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hsh = defaultdict(int)
        for i in nums:
            hsh[i] += 1
        for i in hsh:
            if hsh[i] > len(nums)/2:
                return i
        