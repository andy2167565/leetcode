class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        children = {}  # Store the number of file names that share the same root
        for name in names:
            last = name
            if name in children:
                k = children[name]
                while last in children:  # Find the last file name with the same root of name
                    k += 1
                    last = f'{name}({k})'
                children[name] = k
            children[last] = 0
        return children.keys()
