class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)-1
        col = len(matrix[0])-1

        i = 0
        j = row

        while i <= row:
            arr = matrix[i]
            if arr[-1] >= target:
                l = 0
                r = col
                while l <= r:
                    mid = (l+r)//2
                    if arr[mid] == target:
                        return True
                    elif arr[mid] > target:
                        r = mid -1
                    else:
                        l = mid + 1
                
            i += 1

        return False

        