class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # form hash map containing anagram lists
        anagrams = {}
        for s in strs:
            s_sorted = str(sorted(s))
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
        
        # form sublists from hash map
        res = [anagrams[k] for k in anagrams]
        return res
        