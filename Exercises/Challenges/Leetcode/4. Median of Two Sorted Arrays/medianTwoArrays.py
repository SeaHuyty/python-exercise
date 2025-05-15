class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        # Merge array
        merge = nums1 + nums2
        # Sort the merged array
        merge.sort()
        # Calculate the number of elements in the array.
        elements = len(merge)
        # If the number of elements in the merged array is an odd number.
        if (elements % 2) == 1:
            return (merge[elements//2])
        # If the number of elements in the merged array is an even number.
        else:
            return ((merge[elements//2] + merge[elements//2 - 1]) / 2)