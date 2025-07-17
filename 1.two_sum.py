class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = []
        for i in range(len(nums)):
            num1 = nums[i]
            for x in range(i+1, len(nums)):
                num2 = nums[x]
                if num1 + num2 == target:
                    d.append(i)
                    d.append(x)
                    return d
                else:
                    continue
        return False
