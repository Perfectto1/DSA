class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        for index, num in enumerate(sorted(list(set(nums)))):
            if num == target:
                return index