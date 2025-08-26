from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return nums[0]
        l = 0
        r = len(nums)
        mid = r // 2
        while l < mid:
            print(nums[target])
            if target > nums[mid]:
                l = mid
                mid = (l + r) // 2
            elif target < nums[mid]:
                r = mid
                mid = (l + r) // 2
            else:
                return mid
        return -1
print(Solution().search([-1,0,3,5,9,12],3))