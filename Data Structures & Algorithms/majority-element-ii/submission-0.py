class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hshmp = defaultdict(int)
        soln=[]
        for i in nums:
            hshmp[i] +=1
            if hshmp[i] > len(nums)//3 and i not in soln:
                soln.append(i)
        return soln