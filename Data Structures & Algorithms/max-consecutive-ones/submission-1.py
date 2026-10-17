class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ## plan?
        ## counter - update only if find larger count
        ##pointer that goes until very end
        counter = 0
        maxcount = 0
        for i in nums:
            if i == 1:
                counter +=1
                maxcount = max(maxcount, counter)
            else:
                counter = 0
        return maxcount