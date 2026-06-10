class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arraysum = sum(nums)
        return arraysum % k