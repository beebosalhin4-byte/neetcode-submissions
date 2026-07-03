class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sol = set(nums)
        if len(sol)<len(nums):
            return True
        return False