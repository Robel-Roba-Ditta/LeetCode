class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        left = 0
        count = 0
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[left])
                left += 1
            sset.add(s[r])
            count = max(count, r -left +1)
        return count 