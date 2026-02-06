class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        res = 0
        for w in words:
            x = Counter(w)
            for i in range(len(w)):
                if x[w[i]] > c[w[i]]:
                    break
            else:
                res += len(w)
        
        return res