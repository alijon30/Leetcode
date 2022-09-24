You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.
 

Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
Example 2:

Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
 

Constraints:

1 <= num.length <= 105
num consists of digits.

class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        sett = set(num)
        sorted_list = sorted(sett)
        stack = []
        
        Counters = collections.Counter(num)
        print(sorted_list)
        largest_odd_int = "-1"
        queue = []
        
        for val in sorted_list[::-1]:
            if Counters[val] >= 2 :

                times = Counters[val] // 2
                while times != 0:
                    stack.append(val)
                    times -= 1
            if Counters[val] % 2 == 1:
                if int(largest_odd_int) < int(val):
                    largest_odd_int = val
                    
        print(stack)
        if largest_odd_int != "-1":
            stack.append(largest_odd_int)
        print(stack)
    
        stack_strin = str(int("".join(stack)))
        
        if largest_odd_int == "-1":
            stack_strin += stack_strin[::-1]
        else:
            stack_strin += stack_strin[:-1][::-1]
        
        if stack_strin == "00":
            return "0"
        
        return stack_strin
