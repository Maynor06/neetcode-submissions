class Solution:
    def isPalindrome(self, s: str) -> bool:
        sclean = "".join(c for c in s.lower() if c.isalnum())
        sReversed = sclean[::-1]

        return sclean == sReversed
