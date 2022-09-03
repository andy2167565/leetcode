class Solution:
    def romanToInt(self, s: str) -> int:
#======== <Solution 1> ========#
        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num_list = []
        for char in s[::-1]:
            if num_list and num_list[-1] > roman_char[char]:
                num_list.append(-roman_char[char])
            else:
                num_list.append(roman_char[char])
        return sum(num_list)

#======== <Solution 2> ========#
        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans, prev = 0, 'I'
        for char in reversed(s):
            ans, prev = ans - roman_char[char] if roman_char[prev] > roman_char[char] else ans + roman_char[char], char
        return ans

#======== <Solution 3> ========#
        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans, prev = 0, 0
        for char in s:
            ans += roman_char[char]
            if prev < roman_char[char]:
                ans -= 2 * prev
            prev = roman_char[char]
        return ans

#======== <Solution 4> ========#
        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s.replace('IV', 'IIII')\
             .replace('IX', 'VIIII')\
             .replace('XL', 'XXXX')\
             .replace('XC', 'LXXXX')\
             .replace('CD', 'CCCC')\
             .replace('CM', 'DCCCC')
        return sum(map(roman_char.get, s))

#======== <Solution 5> ========#
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': -2,
            'IX': -2,
            'XL': -20,
            'XC': -20,
            'CD': -200,
            'CM': -200
        }
        return sum(s.count(char) * num for char, num in mapping.items())

#======== <Solution 6> ========#
        return (s.count('CM') + s.count('CD')) * (-200) + (s.count('XC') + s.count('XL')) * (-20) + (s.count('IX') + s.count('IV')) * (-2) + s.count('M') * 1000 + s.count('D') * 500 + s.count('C') * 100 + s.count('L') * 50 + s.count('X') * 10 + s.count('V') * 5 + s.count('I') * 1
