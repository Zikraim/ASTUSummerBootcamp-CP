class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)

        
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]

        ans = inf

      
        for length in range(l, r+1):
            for i in range(n - length + 1):
                s = pre[i+length] - pre[i]
                if s > 0:
                    ans = s if s<ans else ans
                    
        return ans if ans != inf else -1