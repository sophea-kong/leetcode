class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for i in s:
            if(i.isalnum()):
                new_s+=i
        return(new_s[::-1].lower() == new_s.lower())