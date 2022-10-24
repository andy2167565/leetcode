class Solution:
    def defangIPaddr(self, address: str) -> str:
#======== <Solution 1> ========#
        return '[.]'.join(address.split('.'))

#======== <Solution 2> ========#
        return address.replace('.', '[.]')

#======== <Solution 3> ========#
        import re
        return re.sub('\.', '[.]', address)

#======== <Solution 4> ========#
        return ''.join('[.]' if c == '.' else c for c in address)
