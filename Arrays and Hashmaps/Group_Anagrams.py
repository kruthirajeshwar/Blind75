class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_str = defaultdict(list)
        for i in strs:
            sorted_strs = ''.join(sorted(i))
            hash_str[sorted_strs].append(i)
        return list(hash_str.values())
