import collections

class Solution(object):
    def smallestRange(self, nums):
        merged = []

      
        for list_index in range(len(nums)):
            for value in nums[list_index]:
                merged.append((value, list_index))

        merged.sort()

        freq = collections.defaultdict(int)
        left = 0
        covered = 0
        total_lists = len(nums)

        start, end = -100000, 100000

        for right in range(len(merged)):
            value, idx = merged[right]

            if freq[idx] == 0:
                covered += 1
            freq[idx] += 1

            while covered == total_lists:
                if value - merged[left][0] < end - start:
                    start = merged[left][0]
                    end = value

                left_value, left_idx = merged[left]
                freq[left_idx] -= 1

                if freq[left_idx] == 0:
                    covered -= 1

                left += 1

        return [start, end]