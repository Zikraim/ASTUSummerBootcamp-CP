class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros, answer = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            answer = max(answer, i - left)
        
        return answer


