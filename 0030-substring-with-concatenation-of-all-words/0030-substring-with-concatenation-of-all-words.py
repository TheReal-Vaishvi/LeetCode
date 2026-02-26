class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        n = len(s)
        
        if n < total_len:
            return []
        
        from collections import Counter
        
        word_count = Counter(words)
        result = []
        
        # We try starting from each possible offset
        for i in range(word_len):
            left = i
            count = 0
            current_count = {}
            
            for right in range(i, n - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1
                    
                    # If word appears more than needed
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If all words matched
                    if count == total_words:
                        result.append(left)
                        
                        # Move left forward to find next possibility
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # Reset window
                    current_count.clear()
                    count = 0
                    left = right + word_len
        
        return result
        