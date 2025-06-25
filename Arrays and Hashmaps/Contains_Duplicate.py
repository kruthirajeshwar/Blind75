class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set_nums = set(nums)
        # if len(nums) == len(set_nums):
        #     return False
        # return True
        # set_nums = set()
        # for i in nums:
        #     if i in set_nums:
        #         return True
        #     set_nums.add(i)
        # return False
        return len(set(nums)) < len(nums)