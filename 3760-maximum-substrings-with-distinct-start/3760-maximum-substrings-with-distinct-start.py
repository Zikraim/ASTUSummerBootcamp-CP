class Solution:
    def maxDistinct(self, s: str) -> int:
      unique_set = set()
      for char in s:
        if char in unique_set:
            continue
        else:
            unique_set.add(char) 
      return len(unique_set)
        
        