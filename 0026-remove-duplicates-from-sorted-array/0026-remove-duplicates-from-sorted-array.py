class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        j=1

        while(j<len(nums)):
            if(nums[j]!=nums[j-1]):
                nums[i]= nums[j]
                i+=1
            j+=1

        nums = nums[0:i]
        return i
        