class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # form hash map containing anagram lists
        anagrams = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            anagrams[tuple(counts)].append(s)
        
        # form sublists from hash map
        return list(anagrams.values())
        