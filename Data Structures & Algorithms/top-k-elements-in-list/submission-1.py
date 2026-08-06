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

        # loop down from highest possible frequency
        # return when k frequenceis are hit
        res = []
        for i in range(len(nums), -1, -1):
            if i in (count2n):
                for n in count2n[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        
        return res



        