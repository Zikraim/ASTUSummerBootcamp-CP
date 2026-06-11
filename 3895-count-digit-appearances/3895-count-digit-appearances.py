class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
       strnums = str(nums)
       strdigit= str(digit)
       count = 0
       for i in strnums:
        if strdigit in i:
            count +=1
       return count
    
           

        