class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostf = 0
        element =0
        numss = []
        sol = []
        from collections import Counter
        hsh = Counter()
        for i in nums:
            hsh[i] +=1
        for i in hsh:
            numss.append([hsh[i], i])
        numss.sort(reverse = True)
        for i in range(k):
            sol.append(numss[i][1])
        return sol