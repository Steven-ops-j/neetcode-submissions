class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1 
            else:
                cl, cr = 0, len(matrix[mid]) - 1
                while cl <= cr:
                    cmid = (cl + cr) // 2
                    if matrix[mid][cmid] > target:
                        cr = cmid - 1
                    elif matrix[mid][cmid] < target:
                        cl = cmid + 1
                    else:
                        return True
                return False
        return False

