class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t): return False
        count = [0] * 26
        n = len(s)
        for i in range(n):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        for val in count:
            if val != 0:
                return False
        return True

