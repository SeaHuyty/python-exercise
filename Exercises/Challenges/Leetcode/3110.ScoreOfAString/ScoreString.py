class Solution:
    def scoreOfString(self, s: str) -> int:
        l = 0
        ascii_value = {}
        for i in s:
            ascii_value[l] = ord(f'{i}')
            l += 1
        value = 0
        for i in range(l - 1):
            value += abs(ascii_value[i] - ascii_value[i+1])
        return value