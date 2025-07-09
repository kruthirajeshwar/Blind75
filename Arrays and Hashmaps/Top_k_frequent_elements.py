class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        for n, c in hash_map.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res
