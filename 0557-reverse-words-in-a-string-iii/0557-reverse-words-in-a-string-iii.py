class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        length= len(chars)

        start = 0
        while start < length:
            end = start

            while end < length and chars[end] != ' ':
                end += 1

            left, right = start, end - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

            start = end + 1

        return ''.join(chars)