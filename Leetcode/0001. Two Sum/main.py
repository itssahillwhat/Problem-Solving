class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}

        for i in range(n):
            a = nums[i]
            temp = target - a
            if temp in hashmap:
                return [hashmap[temp], i]
            hashmap[a] = i