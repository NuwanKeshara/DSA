class Solution:
    def search(self, nums:list[int], target:int) -> int:
        first, last = 0, len(nums)-1

        while not (first > last):
            mid = (first + last) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = mid - 1
        return -1
    
    # memory overflow fixed BS
    def search(self, nums:list[int], target:int) -> int:
        first, last = 0, len(nums)-1

        while first <= last:
            mid = (first + (last - first)) // 2

            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = mid - 1
            else:
                return mid
            
        return -1
    


    def searchMatrix(self, matrix:list[list[int]], target:int) -> bool:
        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, (rows * columns) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // columns
            column = (mid % columns)

            if matrix[row][column] < target:
                left = mid + 1
            elif matrix[row][column] > target:
                right = mid - 1
            else:
                return True
                  
        return False


    



if __name__ == "__main__":
    sol = Solution()


    # print(sol.evalRPN(["4","13","5","/","+"]))
    # print(sol.search([-1,0,2,4,6,8], 3))

    print(sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 41))