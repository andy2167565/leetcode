class Solution:
    def countAndSay(self, n: int) -> str:
#======== <Solution 1> ========#
        result = '1'
        # Loop n - 1 times since the string for n = 1 is already defined
        while n > 1:
            # Pointer for characters
            char, current = 0, ''
            # Loop for each group in the string
            while char < len(result):
                # Count identical characters in each group
                count = 1
                # char + 1 < len(result): The character next to char is in the range of string
                while char + 1 < len(result) and result[char] == result[char + 1]:
                    count += 1
                    char += 1
                current += str(count) + result[char]
                char += 1
            result = current
            n -= 1
        return result

#======== <Solution 2> ========#
        result = '1'
        for _ in range(n - 1):
            letter, current, count = result[0], '', 0
            for l in result:
                if letter == l:
                    count += 1
                else:
                    current += str(count) + letter
                    letter = l
                    count = 1
            current += str(count) + letter
            result = current
        return result
        
#======== <Solution 3> ========#
        if n == 1: return '1'
        current = self.countAndSay(n - 1)
        char, result = 0, ''
        while char < len(current):
            count = 1
            while char + 1 < len(current) and current[char] == current[char + 1]:
                count += 1
                char += 1
            result += str(count) + current[char]
            char += 1
        return result

#======== <Solution 4> ========#
        import itertools
        result = '1'
        for _ in range(n - 1):
            result = ''.join(str(sum(map(bool, v))) + k for k, v in itertools.groupby(result))
        return result

#======== <Solution 5> ========#
        import re
        result = '1'
        for _ in range(n - 1):
            result = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), result)
        return result

#======== <Solution 6> ========#
        import re
        result = '1'
        for _ in range(n - 1):
            result = ''.join(str(len(group)) + digit for group, digit in re.findall(r'((.)\2*)', result))
        return result
