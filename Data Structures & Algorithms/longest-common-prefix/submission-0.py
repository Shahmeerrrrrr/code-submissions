class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_word = strs[0]
        for i in range(len(first_word)):
            for word in strs[1:]:
                if i >= len(word):
                    return first_word[:i]
                if word[i] != first_word[i]:
                     return first_word[:i]
        return first_word
