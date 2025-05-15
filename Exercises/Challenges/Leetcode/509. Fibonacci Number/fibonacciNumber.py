class Solution:
    def fib(self, n: int) -> int:
        # Recursive Function: a recursive function is one that calls itself in order
        #                     to solve a problem.
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)
        value = fibonacci(n)
        return value