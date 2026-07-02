class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) / 2
        hm = {}
        for x in nums:
            hm[x] = hm.get(x, 0) + 1
            if hm[x] > threshold:
                return x


            