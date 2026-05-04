class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        ans = []
        counts = []
        for i in range(len(strs)):
            f1 = {}
            for j in range(len(strs[i])):
                f1[strs[i][j]] = 1 + f1.get(strs[i][j], 0)
            counts.append(f1)

        for i in range(len(strs)):
            if counts[i] != {'': -1}:
                arr = [strs[i]]
                for k in range(i + 1, len(strs)):
                    flag = True
                    for j in range(len(strs[i])):
                        if len(strs[i]) != len(strs[k]):
                            flag = False
                            break
                        if counts[i].get(strs[i][j], 0) != counts[k].get(strs[i][j], 0):
                            flag = False
                            break
                    if flag and len(strs[i]) == len(strs[k]):
                        counts[k] = {'': -1}
                        arr.append(strs[k])
                ans.append(arr)
                counts[i] = {'': -1}

        return ans
