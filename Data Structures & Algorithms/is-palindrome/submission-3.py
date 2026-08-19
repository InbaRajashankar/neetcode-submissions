import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = "".join(
            char.lower()
            for char in s
            if char.isascii() and char.isalnum()
        )
        left = 0
        right = len(s_lower) - 1
        while left < right:
            if s_lower[left] != s_lower[right]:
                return False
            left += 1
            right -= 1
        
        return True
        