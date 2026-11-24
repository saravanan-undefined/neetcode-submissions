class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        i, j = 0, 0
        res = 0
        while i < l1 and j < l2:
                if s[i] == t[j]:
                    i += 1
                    res += 1
                else:
                    pass
                j += 1
                
        return res == l1