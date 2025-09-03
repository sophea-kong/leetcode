class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_set = set()
        for i in nums[:]:
            if(i not in temp_set):
                temp_set.add(i)
            else :
                nums.remove(i)
        return len(nums)
