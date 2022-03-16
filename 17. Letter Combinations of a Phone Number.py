Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
  
  class Solution:
    def letterCombinations(self, digits: str):
        combinations = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if digits == "":
            return []

        numbers = list(combinations[digits[0]])

        for digit in digits[1:]:
            numbers = [old + new for old in numbers for new in list(combinations[digit[0]])]
        return numbers
      
      
