class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_value = nums[0]
        for i in range(len(nums)):
            if (abs(nums[i]) < abs(closest_value)) or (abs(nums[i]) == abs(closest_value) and nums[i] > closest_value):
                closest_value = nums[i]
            print(closest_value)
        return closest_value