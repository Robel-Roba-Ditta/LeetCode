class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}
        
        for s in strs:
            key = tuple(sorted(s))
            if key not in anagram_dict:
                anagram_dict[key] = []
            anagram_dict[key].append(s)
            
        return list(anagram_dict.values())
        