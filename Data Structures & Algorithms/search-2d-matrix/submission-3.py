class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)-1
        COL = len(matrix[0])-1

        i = 0
        j = ROWS

        while i <= j:
            row = (i + j)//2
            if matrix[row][0] > target:
                j = row - 1
            elif matrix[row][-1] < target:
                i = row + 1
            else:
                break

        if not (i<=j):
            return False

        row = (i + j)//2
        l = 0
        r = len(matrix[row])-1
        arr = matrix[row]

        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid -1
            else:
                l = mid + 1

        return False

        