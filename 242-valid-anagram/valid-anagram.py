class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1

        for i in t:
            if i in s_dict:
                if s_dict[i] == 1:
                    del s_dict[i]
                else:
                    s_dict[i] -= 1
            else:
                return False
        return not s_dict
