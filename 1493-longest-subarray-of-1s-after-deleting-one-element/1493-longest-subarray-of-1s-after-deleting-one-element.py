class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0 
        right = -1 
        max_length =0 
        for i in range (len(nums)):
            if nums[i] == 0 :
                left = right+1
                right = i 
            max_length = max  (max_length, i-left)
        return max_length
    
        

