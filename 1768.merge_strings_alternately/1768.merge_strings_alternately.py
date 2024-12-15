class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = [] 
        i = 0
        if len(word1)>len(word2):
            length = len(word2) 
        else:
            length = len(word1)
        while i < length:
            word.append(word1[i])
            word.append(word2[i])
            i += 1
        word.extend(word1[i:])
        word.extend(word2[i:])
        return ''.join(word)