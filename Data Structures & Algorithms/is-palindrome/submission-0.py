class Solution:
    def isPalindrome(self, s: str) -> bool:
        strings = [c.lower() for c in s if c.isalnum()]
        i, j = 0, len(strings) - 1
        while i < j:
            if strings[i] != strings[j]:
                return False
            i += 1
            j -= 1
        return True