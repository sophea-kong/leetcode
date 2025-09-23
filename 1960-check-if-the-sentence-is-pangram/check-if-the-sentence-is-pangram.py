class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        hash_map = set('abcdefghijklmnopqrstuvwxyz')
        sent_set = set(sentence)
        return hash_map == sent_set