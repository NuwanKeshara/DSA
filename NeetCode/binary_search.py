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
    




if __name__ == "__main__":
    sol = Solution()


    # print(sol.evalRPN(["4","13","5","/","+"]))
    print(sol.search([-1,0,2,4,6,8], 3))