class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text_s = text.split()
        broken = set(brokenLetters)
        count = 0
        for i in text_s:
            broke = False
            for j in i:
                if j in broken:
                    broke = True
                    break
            if (not broke):
                count += 1
        return count