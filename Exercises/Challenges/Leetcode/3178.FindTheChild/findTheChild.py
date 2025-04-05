class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        child = 0
        for i in range(k):
            if child == (n - 1):
                flag = 0
            elif child == 0:
                flag = 1
            if flag == 1:
                child += 1
            elif flag == 0:
                child -= 1
        return child