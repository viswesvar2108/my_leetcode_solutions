class Solution(object):
    #two pointer technique
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the list first
        res = []
        length = len(nums)
        
        for i in range(length - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, length - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip the same element to avoid duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    #moving forward
                    left += 1
                    #moving backward
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return res
