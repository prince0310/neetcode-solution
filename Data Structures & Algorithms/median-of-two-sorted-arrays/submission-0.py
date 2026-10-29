class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # left = 0
        # right = 0
        # sorted_array = []

        # while left <  len(nums1)  and right <  len(nums2):
        #     if nums1[left] <= nums2[right]:
        #         sorted_array.append(nums1[left])
        #         left += 1
        #     else:
        #         sorted_array.append(nums2[right])
        #         right += 1
        
        # sorted_array.extend(nums1[left:])
        # sorted_array.extend(nums2[right:])
        
        # n = len(sorted_array)


        # if n%2 == 0:
        #     return (sorted_array[n//2] + sorted_array[(n//2) - 1])/2
        # else:
        #     return (sorted_array[n//2])

        A , B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(B) < len(A):
            B, A = A, B


        left = 0 
        right = len(A) - 1


        while True:

            i = (left + right)//2 # for A 

            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
        
            if Aleft <= Bright and Bleft <= Aright:
                if (total) % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright) )/2
            elif Aleft > Bright:
                right = i - 1
            
            else:
                left = i + 1








        