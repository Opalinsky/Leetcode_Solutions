class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,}
        int = []
        roman_to_int = []
        for i in range(len(s)):
            if s[i] in dict.keys():
                char = dict.get(s[i])
                int.append(char)
        print(int)
        i = 0
        while i < len(int):
            if i == (len(int)-1):
                roman_to_int.append(int[-1])
                break 
            element = int[i] 
            next_element = int[i+1]
            if next_element > element:
                next_element = next_element - element 
                roman_to_int.append(next_element)
                i += 2
            else:
                roman_to_int.append(element)
                i += 1
        print(roman_to_int)
        return sum(roman_to_int)