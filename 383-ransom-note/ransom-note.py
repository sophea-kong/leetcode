class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def intoDict(note):
            note_dict = dict()
            for i in note:
                if not i in note_dict:
                    note_dict[i] = 1
                else : 
                    note_dict[i] += 1
            return note_dict
        maga_dict = intoDict(magazine)
        for i in ransomNote:
            if i in maga_dict and maga_dict[i] == 1:
                del maga_dict[i]
            elif (i in maga_dict and not maga_dict[i] == 1):
                maga_dict[i] -= 1
            else:
                return False
        return True
                