class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s = [""] * n
        for i in range(1, n+1):
            if (i % 5 == 0) and (i % 3 == 0):
                s[i - 1] = "FizzBuzz"
            elif (i % 5 == 0):
                s[i - 1] = "Buzz"
            elif (i % 3 == 0):
                s[i - 1] = "Fizz"
            else:
                s[i - 1] = f"{i}" 
        return s