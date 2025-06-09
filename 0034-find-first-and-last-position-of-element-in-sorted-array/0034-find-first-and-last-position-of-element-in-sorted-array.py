class Solution(object):
    def searchRange(self, nums, target):
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    index = mid
            return index
        
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    index = mid
            return index

        return [findLeft(nums, target), findRight(nums, target)]
