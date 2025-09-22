class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = defaultdict(int)
        for i in s:
            hash_map[i] += 1
        for i in range(len(s)):
            if (hash_map[s[i]] == 1):
                return i
        return -1
        