Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

class Solution:
    def partitionString(self, s: str) -> int:
        
        
        window_start = 0
        min_length = 0
        char_freq = {}
        
        
        for window_end in range(len(s)):
            current = s[window_end]
            
            if current not in char_freq:
                char_freq[current] = 1
                
            else:
                min_length += 1
                
                while len(char_freq) != 0:
                    left = s[window_start]
                    
                    if left in char_freq:
                        del char_freq[left]
                    
                    window_start += 1
                    
                char_freq[current] = 1
                
        return min_length + 1
      
      
      
      
