class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        left=0
        length=1
        answer=1
        for right in range(1,len(prices)):
            if prices[left]-prices[right] == 1:
                length+=1
            else:
                length=1
            answer+=length
            left+=1
        return answer
                




        