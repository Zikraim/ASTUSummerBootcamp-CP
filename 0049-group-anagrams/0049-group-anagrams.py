from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map= defaultdict(list)
        for i in strs:
            count =[0]*26
            for j in i:
                count[ord(j)-ord('a')] +=1

            key =tuple(count) 
            map[key].append(i)
        return list(map.values())

        





        