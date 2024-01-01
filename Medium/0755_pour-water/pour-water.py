class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        while volume:
            curr_height, fill, l = heights[k], k, k - 1
            while l >= 0:  # Find the first lowest level on the left side
                if heights[l] > curr_height:
                    break
                if heights[l] < curr_height:
                    curr_height = heights[l]
                    fill = l
                l -= 1
            if fill == k:  # Cannot move left
                r = k + 1
                while r < len(heights):  # Find the first lowest level on the right side
                    if heights[r] > curr_height:
                        break
                    if heights[r] < curr_height:
                        curr_height = heights[r]
                        fill = r
                    r += 1
            heights[fill] += 1
            volume -= 1
        return heights
