class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        
        odd_char = ""
        odd_count = 0
        
        for ch in freq:
            if freq[ch] % 2 == 1:
                odd_count += 1
                odd_char = ch
                if odd_count > 1:
                    return ""
        
        left = []
        
        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))
        
        left_half = "".join(left)
        right_half = left_half[::-1]
        
        middle = odd_char if odd_count == 1 else ""
        
        return left_half + middle + right_half
