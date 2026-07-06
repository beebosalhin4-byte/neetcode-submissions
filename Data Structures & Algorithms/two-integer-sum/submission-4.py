class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshtb = []
        for i, val in enumerate(nums):
            hshtb.append([val,i])
        hshtb.sort()
        i = 0
        j = len(nums) - 1
        while i< j:
            if hshtb[i][0] + hshtb[j][0] == target and hshtb[i][1] != hshtb[j][1]:
                return [min(hshtb[i][1], hshtb[j][1]), max(hshtb[i][1], hshtb[j][1])]
            if hshtb[i][0] + hshtb[j][0] < target:
                i += 1
            if hshtb[i][0] + hshtb[j][0] > target:
                j -=1