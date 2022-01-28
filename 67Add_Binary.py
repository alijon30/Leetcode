Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"





class Solution:
    def addBinary(self, a: str, b: str):
        lst = []
        power = 0
        sum1 = 0
        sum2 = 0
        for i in range(len(a)-1, -1, -1):
            if a[i] != '0':
                sum1 += 2 ** power
            power += 1
        power = 0
        for i in range(len(b)-1, -1, -1):
            if b[i] != '0':
                sum2 += 2 ** power
            power += 1
        final_num = sum1 + sum2
        print(final_num)
        if final_num == 0:
            return "0"
        while final_num >= 1:
            remainder = final_num % 2
            lst.append(str(remainder))
            final_num = final_num //2
        lst.reverse()
        return "".join(lst)
