class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if nums: 
            if lower < nums[0]:
                res.append([lower, nums[0]-1]) 
        else:
            res.append([lower, upper])

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append([nums[i-1]+1, nums[i]-1])
        if nums and nums[-1] < upper:
            res.append([nums[-1]+1, upper])

        return res