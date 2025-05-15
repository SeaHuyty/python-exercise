class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return (haystack.find(f"{needle}"))
        else:
            return -1