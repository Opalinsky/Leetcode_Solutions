class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1
                print(index, len(s))
                if index == len(s):
                    return True
        return False 
                