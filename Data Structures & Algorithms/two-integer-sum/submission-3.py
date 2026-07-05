class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmap = {}
        for i, n in enumerate(nums):
            hshmap[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hshmap and hshmap[diff] != i:
                return [i, hshmap[diff]]
        return []