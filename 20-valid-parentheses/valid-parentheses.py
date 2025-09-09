class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_stk = list()
        hsh = {')':'(','}':'{',']':'['}
        for i in s:
            if i in hsh.values():
                open_stk.append(i)
            else:
                if(open_stk and open_stk[-1]==hsh[i]):
                    open_stk.pop()
                else:
                    return False
        return not open_stk