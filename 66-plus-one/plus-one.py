class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        power = 0
        nums = 0
        for i in digits[::-1]:
            nums += i * (10**power)
            power+=1
        nums += 1
        result = []
        for i in range(len(str(nums))):
            result.append(int(str(nums)[i]))
        return result


        