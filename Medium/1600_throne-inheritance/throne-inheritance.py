import collections
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family = collections.defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(curr, inheritance=[]):
            if curr not in self.dead:
                inheritance.append(curr)
            for child in self.family[curr]:
                dfs(child, inheritance)
            return inheritance
        return dfs(self.king)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
