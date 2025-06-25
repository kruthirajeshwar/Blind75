class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
         map = {}
         start = 0
         max_len = 0
         for end in range(len(s)):
             if s[end] in map and map[s[end]]>=start:
                 start = map[s[end]]+1
             map[s[end]] = end
             max_len = max(max_len, end-start+1)
         return max_len  
