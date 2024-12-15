class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            seen.add(local.split('+')[0].replace('.', '') + '@' + domain)
        return len(seen)
