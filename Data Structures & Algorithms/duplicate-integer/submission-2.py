class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sol = set()
        for num in nums:
            if num in sol:
                return True
            sol.add(num)
        return False