class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while (not s[left].isalnum()) and left < right:
                left += 1
            while (not s[right].isalnum()) and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
    

    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.isalphanum(s[left]):
                left += 1
            while left < right and not self.isalphanum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            right += 1
            left -= 1
        return True
    
    def isalphanum(self, s: str) -> bool:
        return ( (ord("0") <= ord(s) <= ord("9")) or 
                 (ord("a") <= ord(s) <= ord("z")) or
                 (ord("A") <= ord(s) <= ord("Z")) )
    

    def isPalindrome3(self, s: str) -> bool:
        new_s = ""

        for i in s.lower():
            if i.isalnum():
                new_s += i

        return new_s == new_s[::-1]
    


    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0,len(numbers)-1
        
        while left < right:
            while (left < right) and ((numbers[left] + numbers[right]) > target):
                right -= 1
            while (left < right) and ((numbers[left] + numbers[right]) < target):
                left += 1
            if (numbers[left] + numbers[right] == target) and left < right:
                return [left+1, right+1]
            right -= 1
        return [-1, -1]
        
    
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        left , right = 0, len(numbers)-1

        while left < right:
            two_sum = numbers[left] + numbers[right]
            
            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                return [left+1, right+1]
        
        return [-1,-1]
    
    

if __name__ == "__main__":

    cls = Solution()
    print(cls.twoSum2([1,2,3,4],3))