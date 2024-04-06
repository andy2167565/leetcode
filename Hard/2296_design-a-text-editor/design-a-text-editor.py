class TextEditor:

    def __init__(self):
        self.s = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        prev, self.cursor = self.cursor, max(0, self.cursor - k)
        self.s = self.s[:self.cursor] + self.s[prev:]
        return k if prev - k >= 0 else prev

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        return self.s[max(0, self.cursor - 10): self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.s), self.cursor + k)
        return self.s[max(0, self.cursor - 10): self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
