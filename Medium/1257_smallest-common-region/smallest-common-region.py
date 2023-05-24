class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {region[i]: region[0] for region in regions for i in range(1, len(region))}  # Build the family tree
        ancestor_history = {region1}
        while region1 in parents:  # Store all ancestors of region1
            region1 = parents[region1]
            ancestor_history.add(region1)
        while region2 not in ancestor_history:  # Retrieve ancestors of region2 by family tree until we find the first common ancestor in ancestor history of region1
            region2 = parents[region2]
        return region2
