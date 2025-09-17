class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_hash = defaultdict()
        for i in range(len(nums)):
            if nums[i] not in nums_hash:
                nums_hash[nums[i]] = i
            else:
                if abs(i-nums_hash[nums[i]]) <= k:
                    return True
                else:
                    nums_hash[nums[i]] = i
        return False
        