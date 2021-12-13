class Solution:
    def MedianOfFinalArray(finalArray):
        mid_val = len(finalArray) // 2
        if len(finalArray) % 2 == 0:
            return (finalArray[mid_val - 1] + finalArray[mid_val]) / 2
        else:
            return (finalArray[mid_val])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        l_nums1, l_nums2 = len(nums1), len(nums2)

        if l_nums1 == 0 and l_nums2 == 0:
            return 0.00
        elif l_nums1 == 0:
            return Solution.MedianOfFinalArray(nums2)
        elif l_nums2 == 0:
            return Solution.MedianOfFinalArray(nums1)
        else:
            finalArray = []
            while i < l_nums1 and j < l_nums2:

                if nums1[i] > nums2[j]:
                    finalArray.append(nums2[j])
                    j += 1
                else:
                    finalArray.append(nums1[i])
                    i += 1
            finalArray = finalArray + nums1[i:] + nums2[j:]
            return Solution.MedianOfFinalArray(finalArray)


"""
Time Complexity:  O(n) + O(m)
    Since we are using merge sort here and the time complexity for merge sort is O(nlog n) to the base 2.
    
    Since we are using M and n here it will be O(log(m+n)

Space Complexity: Since we are storing in it temporary variable. 
                == O(m+n)    
    




"""