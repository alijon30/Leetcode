Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
  
  
  class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(l, r):
            i = 0
            j = 0
            res = []
            
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1
            
            while i < len(l):
                res.append(l[i])
                i += 1
            while j < len(r):
                res.append(r[j])
                j += 1
            return res
        complete = merge(nums1, nums2)
        if len(complete) % 2 != 0:
            return complete[len(complete)//2]
        else:
            return (complete[math.floor(len(complete)/2)] + complete[math.ceil(len(complete)/2)-1])/2
          
          
