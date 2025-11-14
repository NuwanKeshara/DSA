
def v_binary_search(nums: list[int], target: int) -> int:
    left , right = 0 , len(nums)-1
    
    while left <= right:
        mid = (left + right ) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def first_true (arr: list[bool]) -> int:
    left , right = 0 , len(arr)-1
    best_case = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid]:
            best_case = mid
            right = mid - 1
        else:
            left = mid + 1

    return best_case


def rotated_sorted_array(nums: list[int]) -> int:
    left , right = 0 , len(nums)-1
    best_case = -1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] <= nums[-1]:
            best_case = mid
            right = mid - 1
        else:
            left = mid + 1
    return best_case
