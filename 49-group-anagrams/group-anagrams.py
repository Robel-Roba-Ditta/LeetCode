class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for word in strs:
            s = "".join(sorted(word))
            g[s].append(word)
        return list(g.values())