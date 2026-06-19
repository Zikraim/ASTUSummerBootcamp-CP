class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curwindowavg=sum(nums[:k])
        maxavg=curwindowavg
        for i in range(k,len(nums)):
            curwindowavg+= nums[i]
            curwindowavg-=nums[i-k]
            maxavg= max(maxavg, curwindowavg)
        return maxavg/k
        
        