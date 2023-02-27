class FileSystem:

    def __init__(self):
        self.trie = {}

    def ls(self, path: str) -> List[str]:
        node, dirs = self.trie, list(filter(None, path.split('/')))
        for dir in dirs:
            node = node.setdefault(dir, {})
        if type(node) == str:  # path is a file path
            return [dirs[-1]]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        node, dirs = self.trie, list(filter(None, path.split('/')))
        for dir in dirs:  # e.g. path = '/a/b/c', self.trie = {a: {b: {c: {}}}}
            node = node.setdefault(dir, {})

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, dirs = self.trie, list(filter(None, filePath.split('/')))
        filename = dirs.pop()
        for dir in dirs:
            node = node.setdefault(dir, {})
        node[filename] = node.get(filename, '') + content

    def readContentFromFile(self, filePath: str) -> str:
        node, dirs = self.trie, list(filter(None, filePath.split('/')))
        filename = dirs.pop()
        for dir in dirs:
            node = node.setdefault(dir, {})
        return node[filename]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
