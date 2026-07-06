class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hshtb = defaultdict(list)
        for s in strs:
            code=[0]*26
            for l in s:
                code[ord(l)-ord('a')] +=1
            hshtb[tuple(code)].append(s)
        return list(hshtb.values())