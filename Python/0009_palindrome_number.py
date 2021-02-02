"""
1. Get the reverse number.
2. Time complexity is O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10
        
        return x == reverse

if __name__ == "__main__":
    x = 121
    s = Solution()
    print(s.isPalindrome(x))