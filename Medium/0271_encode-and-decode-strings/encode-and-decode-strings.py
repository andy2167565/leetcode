class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(chr(len(s)) + s for s in strs)  # Encode length of string as ASCII character

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs, i = [], 0
        while i < len(s):
            l = ord(s[i])  # Decode length of string
            i += 1
            strs.append(s[i:i+l])
            i += l
        return strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
