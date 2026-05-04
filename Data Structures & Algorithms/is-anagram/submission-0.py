class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        clean_s = "".join(c.lower() for c in s if c.isalnum())
        clean_t = "".join(c.lower() for c in t if c.isalnum())

        return sorted(clean_s) == sorted(clean_t)
        