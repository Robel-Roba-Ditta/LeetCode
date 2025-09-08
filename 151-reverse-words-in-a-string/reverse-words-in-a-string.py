class Solution:
    def reverseWords(self, s):
        s = s.strip()
        words = s.split()
        words = words[::-1]
        reversed_str = ' '.join(words)
        return reversed_str