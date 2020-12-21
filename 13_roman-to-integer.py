class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman_num = list(s)[::-1]
        num_list = []
        
        for char in roman_num:
            if num_list and num_list[-1] > roman_char[char]:
                num_list.append(-roman_char[char])
            else:
                num_list.append(roman_char[char])
        
        return sum(num_list)
