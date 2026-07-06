class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hshmp = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            listt= hshmp[sorteds]
            listt.append(s)
        return list(hshmp.values())