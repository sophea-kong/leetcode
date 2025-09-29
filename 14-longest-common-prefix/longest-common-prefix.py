class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = len(strs[0])
        min_index = 0
        if (len(strs) == 1):
            return strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_index = i
        for i in range(len(strs[min_index])):
            for j in range(len(strs)):
                if strs[min_index][i] != strs[j][i]:
                    return strs[min_index][:i]
        return strs[min_index]

        