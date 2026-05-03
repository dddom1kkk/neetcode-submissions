class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss, tt = {}, {}
        for i in range(len(s)):
            ss[s[i]] = 1 + ss.get(s[i], 0)
            tt[t[i]] = 1 + tt.get(t[i], 0)
        for i in range(len(s)):
            if ss[s[i]] != tt.get(s[i], 0):
                return False
        return True
        # c = s
        # for j in t:
        #     for i in c:
        #         if j == i:
        #             print(j, i)
        #             c = c.replace(j, '', 1)
        #             break
        # if len(c) == 0:
        #     return True
        # return False