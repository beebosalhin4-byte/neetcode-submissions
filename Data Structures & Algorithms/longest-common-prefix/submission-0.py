class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs, key= len)
        for i in range(len(mini)):
            for j in range(len(strs)):
                if strs[j][i] != mini[i]:
                    return mini[0:i]
        return mini