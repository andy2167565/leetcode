class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Reference: https://leetcode.com/problems/satisfiability-of-equality-equations/solutions/234486/java-c-python-easy-union-find/
        def find(letter):
            if letter != parent[letter]:
                parent[letter] = find(parent[letter])
            return parent[letter]
        parent = {letter: letter for letter in map(chr, range(97, 123))}
        for x, e, _, y in equations:  # Iterate all '==' equations and connect equal letters in the same union
            if e == '=':
                parent[find(x)] = find(y)
        return not any(e == '!' and find(x) == find(y) for x, e, _, y in equations)  # Iterate all '!=' inequations and check if any contradiction exists
