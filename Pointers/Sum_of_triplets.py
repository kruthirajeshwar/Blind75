#3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []        
        nums.sort()       
        for i, x in enumerate(nums):
            if (i > 0 and x == nums[i-1]):
                continue
            left = i+1
            right = len(nums)-1
            while(left<right):
                sum = x + nums[left] + nums[right]
                if(sum>0):
                    right = right-1
                elif(sum<0):
                    left=left+1
                else:
                    res.append([x, nums[left], nums[right]])
                    left = left+1
                    while(nums[left]==nums[left-1] and left<right):
                        left = left+1
        return res
