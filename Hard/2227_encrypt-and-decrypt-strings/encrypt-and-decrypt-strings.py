class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc = {k: v for k, v in zip(keys, values)}
        self.dict = dictionary

    def encrypt(self, word1: str) -> str:
        ans = ''
        for c in word1:
            if c not in self.enc:
                return ''
            ans += self.enc[c]
        return ans

    def decrypt(self, word2: str) -> int:
        return sum(self.encrypt(w) == word2 for w in self.dict)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
