from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return i == n
            return dp(i + 1) + dp(i + 2)
        return dp(0)