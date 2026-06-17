class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1= len(nums1)
        length2 = len(nums2)
        i =0
        j=0
        intersect= set()

        while i<length1 and j<length2:
            if nums1[i]==nums2[j]:
                intersect.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
              j+=1
        result=[]
        for num in intersect:
            result.append(num)
        return result

        