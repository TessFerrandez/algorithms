from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        actual_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_parts = local_name.split('+')
            local_name = local_parts[0]
            local_name = local_name.replace('.', '')
            actual_email = local_name + '@' + domain_name
            actual_emails.add(actual_email)
        return len(actual_emails)


solution = Solution()
assert solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
assert solution.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]) == 3
