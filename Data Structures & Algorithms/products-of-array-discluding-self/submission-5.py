class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        factor= 1
        count = 0
        index = 0
        sol = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                count +=1
                index = i
            else:
                factor *=nums[i]
        if count >=2:
            return sol
        elif count == 1:
            sol[index] = factor
            return sol
        else:
            for i in range(len(nums)):
                sol[i] = factor//nums[i]
            return sol

