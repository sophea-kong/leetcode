class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result_list = list()
        total = 0
        for i in operations: 
            if i == "C":
                if result_list:
                    result_list.pop()
            elif i == "D":
                result_list.append(result_list[-1]*2)
            elif i=="+":
                result_list.append(result_list[-1]+result_list[-2])
            else :
                result_list.append(int(i))
        for i in result_list:
            total += i
        return total