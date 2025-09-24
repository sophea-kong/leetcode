class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        if len(ver1) > len(ver2):
            for i in range(abs(len(ver1)-len(ver2))):
                ver2.append("0")
        else:
            for i in range(abs(len(ver1)-len(ver2))):
                ver1.append("0")
        for i in range(len(ver1)):
            if(int(ver1[i]) == int(ver2[i])):
                continue
            elif(int(ver1[i]) > int(ver2[i])):
                return 1
            else:
                return -1
        return 0
        