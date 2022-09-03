class Solution:
    def intToRoman(self, num: int) -> str:
#======== <Solution 1> ========#
        roman_char = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        ans = ''
        for char, val in roman_char.items():
            count, num = divmod(num, val)
            ans += char * count
        return ans

#======== <Solution 2> ========#
        roman_char = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        ans = ''
        for char, val in roman_char.items():
            while num >= val:
                ans += char
                num -= val
            if not num: return ans

#======== <Solution 3> ========#
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return M[num // 1000] + C[(num // 100) % 10] + X[(num // 10) % 10] + I[num % 10]
