class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1
        while lower_bound <= upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            value_at_midpoint = nums[midpoint]
            if target == value_at_midpoint:
                return midpoint
            elif target < value_at_midpoint:
                upper_bound = midpoint - 1
            elif target > value_at_midpoint:
                lower_bound = midpoint + 1
        return -1