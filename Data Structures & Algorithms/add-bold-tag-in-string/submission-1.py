class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n

        for w in words:
            start = s.find(w)
            while start != -1:
                for i in range(start, start + len(w)):
                    bold[i] = True
                start = s.find(w, start + 1)

        res = []
        i = 0
        while i < n:
            if bold[i]:
                res.append("<b>")
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
            else:
                res.append(s[i])
                i += 1
        return "".join(res)



