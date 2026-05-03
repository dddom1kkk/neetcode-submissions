class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c = s
        for j in t:
            for i in c:
                if j == i:
                    print(j, i)
                    c = c.replace(j, '', 1)
                    break
        if len(c) == 0:
            return True
        return False