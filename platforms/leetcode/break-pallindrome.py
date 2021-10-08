class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) <= 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[len(palindrome) - 1] = 'b'
        return ''.join(palindrome)
