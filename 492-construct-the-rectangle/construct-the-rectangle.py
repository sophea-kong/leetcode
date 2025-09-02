class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        all_possible_pair = [[1,1]]
        width = area
        height = 1
        while(width>height):
            width = area/height
            if(area%height==0):
                all_possible_pair.append([width,height])
            height+=1
        return(all_possible_pair[-1])

        