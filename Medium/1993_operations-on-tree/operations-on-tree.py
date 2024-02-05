class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.direct_children = [[] for _ in parent]
        for i, p in enumerate(parent[1:], 1):
            self.direct_children[p].append(i)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user:
            return False
        self.locked.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num not in self.locked:  # num is unlocked
            node = num
            while node != -1:  # Check if num has any locked ancestors
                if node in self.locked:
                    break
                node = self.parent[node]
            else:
                stack, locked_descendant = [num], []
                while stack:
                    node = stack.pop()
                    if node in self.locked:
                        locked_descendant.append(node)
                    for child in self.direct_children[node]:
                        stack.append(child)
                if locked_descendant:  # num has at least one locked descendant
                    self.locked[num] = user  # Lock the given node
                    for node in locked_descendant:  # Unlock all of its descendants
                        self.locked.pop(node)
                    return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
