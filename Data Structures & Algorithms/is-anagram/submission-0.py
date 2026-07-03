class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        for i in s:
            st1.append(i)
        for j in t:
            st2.append(j)
        str1 = st1.sort()
        str2 = st2.sort()
        if st1 == st2:
            return True
        return False