class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i, j = 0, 0
        merged = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2.0
        else:
            return merged[n//2]