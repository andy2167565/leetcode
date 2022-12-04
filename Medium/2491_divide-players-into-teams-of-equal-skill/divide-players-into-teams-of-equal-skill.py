class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
#======== <Solution 1> ========#
        skill.sort()
        chemistry, team_skill = skill[0] * skill[-1], skill[0] + skill[-1]
        for i in range(1, len(skill) // 2):
            if skill[i] + skill[~i] != team_skill:
                return -1
            chemistry += skill[i] * skill[~i]
        return chemistry

#======== <Solution 2> ========#
        import collections
        chemistry, team_skill, counter = 0, 2 * sum(skill) // len(skill), collections.Counter(skill)
        for skill, count in counter.items():
            if count != counter[team_skill - skill]:  # Check if there is the same number of players with paired skill
                return -1
            chemistry += count * skill * (team_skill - skill)
        return chemistry // 2  # Correct double-counted chemistry
