There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.

 

Example 1:

Input: seats = [3,1,5], students = [2,7,4]
Output: 4
Explanation: The students are moved as follows:
- The first student is moved from from position 2 to position 1 using 1 move.
- The second student is moved from from position 7 to position 5 using 2 moves.
- The third student is moved from from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.
Example 2:

Input: seats = [4,1,5,9], students = [1,3,2,6]
Output: 7
Explanation: The students are moved as follows:
- The first student is not moved.
- The second student is moved from from position 3 to position 4 using 1 move.
- The third student is moved from from position 2 to position 5 using 3 moves.
- The fourth student is moved from from position 6 to position 9 using 3 moves.
In total, 0 + 1 + 3 + 3 = 7 moves were used.


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        def merge(L, R):
            i = 0
            j = 0
            
            res = []
            
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    res.append(L[i])
                    i+= 1
                else:
                    res.append(R[j])
                    j +=1
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
        seats = MergeSort(seats)
        students = MergeSort(students)
        count = 0
  
        for i in range(len(students)):
            count += abs(students[i] - seats[i])
        return count
     
     
 class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        def InsertionSort(nums):
            for i in range(1, len(nums)):
                j = i -1
                current = nums[i]
                while j >= 0 and nums[j] > current:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = current
            return nums

        seats = InsertionSort(seats)
        students = InsertionSort(students)
        count = 0
        for i in range(len(students)):
            count += abs(students[i]- seats[i])
        return count
     
     
     
     
     
     
     
     
     
     
     
     
     
     
