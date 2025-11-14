# Fixed size
# Dynamic size

def sub_array_sum(nums: list[int], k: int) -> int:
    sum = 0
    for i in range(k):
        sum += nums[i] 

    for right in range(k,len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]

        sum = max(sum, window_sum)
    return sum


def sub_array_sum1(nums: list[int], k: int) -> int:

    total = 0

    for left in range(len(nums) - k):
        sub_array = nums[left: left+k]
        total = max(total, sum(sub_array))
    return total


# def longest_substring(s: str) -> str:
#     right = left = 0
#     sub_string = ""
#     longest = len(sub_string)

#     for right in range(1,len(s)-1):
#         next_char = s[right]

#         while next_char in sub_string:
#             left += 1
#             sub_string = s[left:right]
#         longest = max(longest, len(sub_string[left:right+1]))

#     return longest

from collections import defaultdict

def longest_subarray(s: str) -> int:
    longest = 0
    left = right = 0
    counter: dict[str,int] = defaultdict(int)

    for right in (1, len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1

        longest = max(longest, right - left + 1)
        
    return longest


def longest_subarray1(s: str) -> int:
    longest = 0
    left = right = 0

    counter: dict[str:int] = {}

    for right in range(1,len(s)):
        if (s[right] not in counter) or (counter[s[right]] == 0):
            counter[s[right]] = 1
        else:
            while counter[s[right]] != 0:
                counter[s[left]] -= 1
                left += 1

        longest = max(longest, right - left + 1)
