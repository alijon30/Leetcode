Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).



class Solution:
    def smallerNumbersThanCurrent(self, nums):
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
            left = MergeSort(array[:round(n / 2)])
            right = MergeSort(array[round(n / 2):])

            return merge(left, right)

        sorted_list = MergeSort(nums)
        ret = []
        i = 1
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                ret.append(sorted_list.index(nums[i]))
            else:
                ret.append(sorted_list.index(nums[i]))
        return ret
