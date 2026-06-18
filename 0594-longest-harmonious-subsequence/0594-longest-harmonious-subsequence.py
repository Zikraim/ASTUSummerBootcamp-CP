
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        maxi = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxi = max(maxi, i - j + 1)
        return maxi

                


        
       

        