class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = defaultdict(int)
        for i in range(len(nums)):
            temp_dict[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in temp_dict and temp_dict[y] != i:
                return [i,temp_dict[y]]