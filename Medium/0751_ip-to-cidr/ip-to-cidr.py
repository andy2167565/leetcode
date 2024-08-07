class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        # Reference: https://leetcode.com/problems/ip-to-cidr/solutions/110219/easy-to-understand-python/
        import math

        def ipToNum(ip):
            components = list(map(int, ip.split('.')))
            return (components[0] << 24) + (components[1] << 16) + (components[2] << 8) + components[3]

        def numToIP(num, mask=(1 << 8) - 1):
            return f'{num >> 24}.{(num >> 16) & mask}.{(num >> 8) & mask}.{num & mask}'

        ans, num = [], ipToNum(ip)
        while n:
            low_bit = num & (-num) if num else 1 << 32
            while low_bit > n:
                low_bit >>= 1
            n -= low_bit
            ans.append(f'{numToIP(num)}/{32 - int(math.log2(low_bit))}')
            num += low_bit
        return ans
