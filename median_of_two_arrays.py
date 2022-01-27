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
    def findMedianSortedArrays(self, nums1, nums2) :
        nums1.extend(nums2)
        print(nums1)
        def merge_sort(array):
            if len(array) <= 1:
                 return array
            middle = len(array)//2
            left, right = merge_sort(array[:middle]), merge_sort(array[middle:])
            return merge(left, right)

        def merge(left, right):
            result = []
            left_pointer, right_pointer = 0, 0

            while left_pointer < len(left) and right_pointer < len(right):
                if left[left_pointer] < right[right_pointer]:
                    result.append(left[left_pointer])
                    left_pointer += 1
                else:
                    result.append(right[right_pointer])
                    right_pointer += 1

            result.extend(left[left_pointer:])
            result.extend(right[right_pointer:])
            return result
        a = merge_sort(nums1)
        if len(a) % 2 == 1:
            return a[len(a)/2]
        else:
            first_index = int(len(a)/2)-1
            second_index = first_index + 1
            return (a[first_index] + a[second_index])/2
