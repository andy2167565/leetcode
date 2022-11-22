class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#======== <Solution 1> ========#
        import collections
        graph = collections.defaultdict(list)
        for acc in accounts:
            name, emails, updated = acc[0], set(acc[1:]), (False, -1)
            for i, s in enumerate(graph[name]):
                if s & emails:  # Common email exists
                    if updated[0]:  # emails have already been merged to previous set
                        graph[name][i].update(graph[name][updated[1]])  # Merge previous set to current set
                        graph[name][updated[1]] = set()  # Make previous set empty
                    else:
                        graph[name][i].update(emails)
                    updated = (True, i)
            if not updated[0]:  # No existing emails connected to name or no common email
                graph[name].append(emails)
        ans = []
        for name, arr in graph.items():
            for emails in arr:
                if emails:
                    ans.append([name] + sorted(emails))
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/accounts-merge/discuss/1084738/Python-The-clean-Union-Find-solution-you-are-looking-for
        import collections
        uf, ownership = UF(len(accounts)), {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:  # email also belongs to previous owner
                    uf.union(i, ownership[email])  # Update parents in uf to connect email to previous owner
                ownership[email] = i
        graph = collections.defaultdict(list)
        for email, owner in ownership.items():
            graph[uf.find(owner)].append(email)  # Append emails to correct index
        return [[accounts[i][0]] + sorted(emails) for i, emails in graph.items()]

class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/accounts-merge/discuss/1601960/C%2B%2BPython-Simple-Solution-w-Images-and-Explanation-or-Building-Graph-and-DFS
        import collections
        graph, seen, ans = collections.defaultdict(list), set(), []
        for acc in accounts:  # Connect nearby emails from the same account
            for i in range(2, len(acc)):
                graph[acc[i]].append(acc[i - 1])
                graph[acc[i - 1]].append(acc[i])
        def dfs(email):  # Collect all emails that are connected to each other
            seen.add(email)
            emailList = [email]
            for neighbor in graph[email]:
                if neighbor not in seen:
                    emailList.extend(dfs(neighbor))
            return emailList
        for acc in accounts:
            if acc[1] not in seen:
                ans.append([acc[0]] + sorted(dfs(acc[1])))
        return ans
