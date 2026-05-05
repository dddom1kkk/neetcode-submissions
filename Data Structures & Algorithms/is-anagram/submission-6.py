class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = defaultdict(list)
        countS = [0] * 26
        countT = [0] * 26
        for i in range(len(s)):
            countS[ord(s[i]) - ord("a")] += 1
            countT[ord(t[i]) - ord("a")] += 1
        ans[tuple(countS)] = s
        ans[tuple(countT)] = t
        if len(ans) != 1:
            return False
        return True