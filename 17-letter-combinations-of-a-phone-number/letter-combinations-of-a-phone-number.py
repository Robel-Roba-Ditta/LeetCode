class Solution:
    def letterCombinations(self, digits):
        length = len(digits)
        if length == 0:
            return []
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return self.dfs(digits, letters, length, [], '', 0)
    
    def dfs(self, digits, letters, length, result, combination, current):
        if current == length:
            result.append(combination)
            return
        for char in letters[digits[current]]:
            self.dfs(digits, letters, length, result, combination+char, current+1)
        return result