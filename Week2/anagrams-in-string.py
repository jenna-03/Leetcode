class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        result = []
        
        p_count = {}
        window_count = {}
        
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        for i in range(len(p)):
            char = s[i]
            window_count[char] = window_count.get(char, 0) + 1
        
        if window_count == p_count:
            result.append(0)
        
        for i in range(len(p), len(s)):
            right_char = s[i]
            window_count[right_char] = window_count.get(right_char, 0) + 1
            
            left_char = s[i - len(p)]
            window_count[left_char] -= 1
            
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            if window_count == p_count:
                result.append(i - len(p) + 1)
        
        return result