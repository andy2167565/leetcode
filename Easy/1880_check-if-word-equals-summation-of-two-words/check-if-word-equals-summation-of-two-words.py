class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
#======== <Solution 1> ========#
        convert = lambda s: int(''.join(str(ord(letter) - 97) for letter in s))
        return convert(firstWord) + convert(secondWord) == convert(targetWord)

#======== <Solution 2> ========#
        table = str.maketrans('abcdefghij', '0123456789')
        return int(firstWord.translate(table)) + int(secondWord.translate(table)) == int(targetWord.translate(table))
