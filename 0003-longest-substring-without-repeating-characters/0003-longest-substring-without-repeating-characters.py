class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()      # store unique characters
        left = 0              # Left pointer of window
        max_length = 0        # Store maximum length
        
        for right in range(len(s)):   # Right pointer moves forward
            
            # If duplicate character found, shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to set
            char_set.add(s[right])
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length