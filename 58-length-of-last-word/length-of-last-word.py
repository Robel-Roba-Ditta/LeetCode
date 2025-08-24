class Solution:
    def lengthOfLastWord(self, s):
        words = s.strip()
        count = 0
        for i in range(len(words)-1, -1, -1):
            if words[i] == " ":
                break
            count += 1
        return count