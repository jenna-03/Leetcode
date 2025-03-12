class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        
        if not s:
            return 0
        
        sign = 1
        start = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            start = 1
        
        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
        
        result *= sign
        result = max(min(result, 2**31 - 1), -2**31)
        
        return result