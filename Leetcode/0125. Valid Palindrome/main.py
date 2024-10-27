class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        def check_palindrome(start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return check_palindrome(start + 1, end - 1)

        return check_palindrome(0, len(s) - 1)