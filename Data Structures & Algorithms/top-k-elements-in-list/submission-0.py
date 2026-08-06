class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # form counts hash map
        n2count = defaultdict(int)
        for n in nums:
            n2count[n]+=1

        # reverse hash map
        count2n = defaultdict(list)
        for n in n2count:
            count2n[n2count[n]].append(n)

        # Sort by count and select top k
        sorted_counts = sorted(count2n.keys(), reverse=True)

        res = []
        for count in sorted_counts:
            for n in count2n[count]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res



        