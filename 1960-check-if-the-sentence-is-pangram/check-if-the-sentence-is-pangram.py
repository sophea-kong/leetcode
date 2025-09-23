class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return set('abcdefghijklmnopqrstuvwxyz') == set(sentence)