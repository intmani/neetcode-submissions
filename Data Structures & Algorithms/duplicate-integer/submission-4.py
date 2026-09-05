class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
            
        coll = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] in coll:
                return True
            else:
                coll.append(nums[i])
        else:
            return False