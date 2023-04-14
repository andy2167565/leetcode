class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {team: [0] * len(votes[0]) + [team] for team in votes[0]}
        for vote in votes:
            for rank, team in enumerate(vote):
                count[team][rank] -= 1
        return ''.join(sorted(votes[0], key=count.get))
