class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
      small=[]
      large=[]
      equal=[]
      for i in nums:
        if i<pivot:
            small.append(i)
        elif i == pivot:
            equal.append(i)
        else: large.append(i)
      return small + equal +large  


        