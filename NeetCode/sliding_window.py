class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0
        min = prices[0]

        for i in prices:
            if min > i:
                min = i
            
            profit = max(profit, i - min)
        
        return profit
    


    def lengthOfLongestSubstring(self, s:str) -> int:
        left, right = 0, 0
        freq_map = {}
        substring, max_substring = 0, 0

        while right < len(s):

            while right < len(s) and freq_map.get(s[right],0) == 0:
                freq_map[s[right]] = 1
                right += 1
                substring += 1
            
            max_substring = max(max_substring, substring)

            while right < len(s) and freq_map.get(s[right]) != 0:
                freq_map[s[left]] -= 1
                substring -= 1
                left += 1

        return max_substring
    

    def lengthOfLongestSubstring2(self, s: str) -> int:

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    



                












if __name__ == "__main__":
    s = Solution()

    print(s.lengthOfLongestSubstring2("abcabcbb"))