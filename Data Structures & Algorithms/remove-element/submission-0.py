class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for i in nums:
            if i != val:
                tmp.append(i)
        k = len(tmp)
        for i in range(k):
            nums[i] = tmp[i]
        return k