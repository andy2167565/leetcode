class Solution:
    def countAndSay(self, n: int) -> str:
#======== <Iterative Solution> ========#
        result = "1"
        # Loop n-1 times since the string for n=1 is already defined
        while n > 1:
            # Pointer for characters
            char = 0
            current = ""
            # Loop for each group in the string
            while char < len(result):
                # Count identical characters in each group
                count = 1
                # char+1 < len(result): The character next to char is in the range of string
                while char+1 < len(result) and result[char] == result[char+1]:
                    count += 1
                    char += 1
                current += str(count) + result[char]
                char += 1
            result = current
            n -= 1
        return result
        
#======== <Recursive Solution> ========#
        if n == 1:
            return "1"
        
        seq = self.countAndSay(n-1)
        
        char = 0
        result = ""
        while char < len(seq):
            count = 1
            while char+1 < len(seq) and seq[char] == seq[char+1]:
                count += 1
                char += 1
            result += str(count) + seq[char]
            char += 1
        return result
