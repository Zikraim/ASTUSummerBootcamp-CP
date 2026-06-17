class Solution:
    def minPairSum(self, nums: List[int]) -> int:
      nums.sort()
      i=0
      j=len(nums)-1
      answer=[]
      while i<j:
         ans=nums[i]+nums[j]
         answer.append(ans)
         i+=1
         j-=1
      return max(answer)
            


        