class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            ans[nums[i]] = 1 + ans.get(nums[i], 0)
        
        print(ans)
        ans = sorted(ans, key = lambda p: ans[p], reverse=True)
        print(ans)
        return ans[0:k]