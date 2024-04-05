class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        import collections
        graph = collections.defaultdict(list)
        for node, parent in enumerate(parents):
            graph[parent].append(node)
        
        def countNodes(node):
            score = subtree_size = 1
            for child in graph[node]:
                count = countNodes(child)
                score *= count
                subtree_size += count
            score *= max(1, len(parents) - subtree_size)  # Number of nodes other than current subtree
            score_count[score] += 1
            return subtree_size
        
        score_count = collections.Counter()
        countNodes(0)
        return score_count[max(score_count)]
