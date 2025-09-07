class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left,right = 0,len(s)-1
        while(left<=right):
            if(not s[left].isalnum()):
                print(s[left])
                left+=1
            elif (not s[right].isalnum()):
                right-=1
            elif (not (s[left].lower() == s[right].lower())):
                return False
            else:
                left+=1
                right-=1
        return True