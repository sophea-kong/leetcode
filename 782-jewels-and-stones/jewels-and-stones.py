class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_set = set(jewels)
        jewel_count = 0
        for i in stones:
            if i in jewel_set:
                jewel_count+=1
        return jewel_count
        