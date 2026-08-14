class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count=0
        start=-1
        lastmin=-1
        lastmax=-1

        for i, num in enumerate(nums):
            if num == minK:
                lastmin = i
            if num == maxK:
                lastmax = i
            if num<minK or num>maxK:
                start= i
                lastmin=i
                lastmax=i
            count+=min(lastmin,lastmax) - start
        return count














