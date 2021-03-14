class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if(x[::-1] ==x): return True
        return False


if __name__ == '__main__':
    s = Solution()
    test = 10
    print(s.isPalindrome(test))