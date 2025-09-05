class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon = "balloon"
        text_dict = defaultdict(int)
        for i in text:
            if i in set(balloon):
                text_dict[i] += 1
        text_dict['l'] = int(text_dict['l']/2)
        text_dict['o'] = int(text_dict['o']/2)
        
        mins = min(text_dict['b'],text_dict['a'],text_dict['l'],text_dict['o'],text_dict['n'])
        return mins
        