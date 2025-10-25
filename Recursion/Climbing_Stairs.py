class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def climb(n,memo):
            if n == 1 or n == 0:
                return 1
            if memo[n] != -1:
                return memo[n]
            memo[n] = climb(n-1,memo) + climb(n-2,memo)
            return memo[n]
        return climb(n,memo)
