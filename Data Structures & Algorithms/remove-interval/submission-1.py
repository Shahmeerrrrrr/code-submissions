class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        s, e = toBeRemoved
        for start, end in intervals:
            if end <= s or start >= e:
                res.append([start, end])
            else:
                if start < s:
                   res.append([start, s])
                if end > e:
                    res.append([e, end]) 
        return res 
