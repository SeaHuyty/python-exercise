class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        flag = None
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
            elif nums[i] == nums[i - 1] and flag != nums[i]:
                flag = nums[i]
                nums[index] = nums[i]
                index += 1
        return index
