class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
#======== <Solution 1> ========#
        import collections
        i, ans = 0, [0] * len(barcodes)
        for barcode, count in collections.Counter(barcodes).most_common():
            for _ in range(count):
                ans[i] = barcode
                i += 2
                if i >= len(barcodes):
                    i = 1
        return ans

#======== <Solution 2> ========#
        import collections
        counter = collections.Counter(barcodes)
        barcodes.sort(key=lambda num: (counter[num], num))
        barcodes[1::2], barcodes[::2] = barcodes[:len(barcodes) // 2], barcodes[len(barcodes) // 2:]
        return barcodes
