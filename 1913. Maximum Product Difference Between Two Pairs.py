The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        def merge(L, R):
            i = 0
            j = 0
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
            n = len(array)
            if n <= 1:
                return array
            
            L = MergeSort(array[: round(n/2)])
            R = MergeSort(array[round(n/2):])
            return merge(L, R)
        sorted_list = MergeSort(nums)
        return sorted_list[-1] * sorted_list[-2] - sorted_list[0] *sorted_list[1]
      
      
      
      
