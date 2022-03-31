Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4









class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def Merge(left, right):
            i = 0
            j = 0
            lst = []
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lst.append(left[i])
                    i += 1
                else:
                    lst.append(right[j])
                    j += 1
                
            while i < len(left):
                lst.append(left[i])
                i += 1
            while j < len(right):
                lst.append(right[j])
                j += 1
            return lst
        
        def MergeList(array):
            n = len(array)
            if n <= 1:
                return array
            
            Left = MergeList(array[:round(n/2)])
            Right = MergeList(array[round(n/2):])
            return Merge(Left, Right)
        
        final = MergeList(nums)
        return final[-k]
      
      
      
      
      
