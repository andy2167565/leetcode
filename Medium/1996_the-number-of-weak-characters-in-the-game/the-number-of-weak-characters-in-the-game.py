class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        import sortedcontainers
        properties.sort()  # Sort by attack
        ans, sl, defenses = 0, sortedcontainers.SortedList(), []
        for i, (attack, defense) in enumerate(properties):
            if not i or properties[i - 1][0] == attack:  # Collect the defenses of characters with the same attack
                defenses.append(defense)
            else:
                for d in defenses:  # Relocate defenses to sl
                    sl.add(d)
                defenses = [defense]  # Reset with defense
            if idx := sl.bisect_left(defense):  # Number of defenses that are weaker than current defense
                ans += idx
                for _ in range(idx):  # Remove the weaker characters to avoid being counted multiple times
                    sl.pop(0)
        return ans
