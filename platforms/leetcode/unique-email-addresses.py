from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sent_to = set()
        for email in emails:
            at_index = email.index("@")
            first_part = email[0:at_index]
            second_part = email[at_index:]
            first_part = first_part.replace(".", "")
            print(first_part)
            plus_index = first_part.find("+")

            if plus_index != -1:
                first_part = first_part[0: plus_index]
            email = first_part + second_part

            sent_to.add(email)
        return len(sent_to)


print(Solution().numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(Solution().numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
print(Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"]))
