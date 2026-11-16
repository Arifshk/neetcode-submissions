class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def code(house: List):
            if len(house) == 1:
                return house[0]
            money = [0] * len(house)
            money[0] = house[0]
            money[1] = max(house[0], house[1])

            for i in range(2, len(house)):
                money[i] = max(money[i-1],house[i]+money[i-2])
            return money[-1]
        return max(code(nums[1:]), code(nums[:-1]))