class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hshtble = [0]*26
        for i in range(len(s)):
            hshtble[ord(s[i])-ord('a')] += 1
            hshtble[ord(t[i])-ord('a')] -= 1
        if hshtble == [0]*26:
            return True
        return False