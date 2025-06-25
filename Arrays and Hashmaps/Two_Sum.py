class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, y in enumerate(nums):
            z = target - y
            if z in dict:
                return [dict[z], i]
            dict[y] = i
