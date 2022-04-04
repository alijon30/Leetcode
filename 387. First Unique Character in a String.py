

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1






class Solution:
    def firstUniqChar(self, s: str) -> int:
        Dict = {}
        
        for item in s:
            if item not in Dict.keys():
                Dict[item] = 1
            else:
                Dict[item] += 1
                
        letter = ""
        for key, value in Dict.items():
            if value == 1:
                letter = key
                break
        return s.index(letter) if letter != "" else -1
      
      
      
