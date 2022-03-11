You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.



class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def merge(L, R):
            i = 0
            j= 0
            res = []
            
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    res.append(L[i])
                    i += 1
                else:
                    res.append(R[j])
                    j += 1
            while i < len(L):
                res.append(L[i])
                i += 1
            
            while j < len(R):
                res.append(R[j])
                j += 1
                
            return res
        def MergeSort(array):
            n= len(array)
            if n <= 1:
                return array
            
            Left= MergeSort(array[: round(n/2)])
            Right = MergeSort(array[round(n/2):])
            
            return merge(Left, Right)
        result = []
        sorted_array = MergeSort(nums)
        for i in range(len(sorted_array)):
            if sorted_array[i] > target:
                break
            if sorted_array[i] == target:
                result.append(i)
                
        return result
      
      
      
      
