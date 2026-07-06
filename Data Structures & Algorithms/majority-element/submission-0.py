class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hshmp = defaultdict(int)
        for val in nums:
            hshmp[val] = hshmp[val] + 1
            if hshmp[val] > len(nums)/2:
                return val
