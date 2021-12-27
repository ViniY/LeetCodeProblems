class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=2:
            return s
        s_rev = s[::-1]  # Reverse the target
        length = len(s)
        l = 0
        r=""
        # for i in range(length):
        #     for j in range(length):
        #         if s[i] == s_rev[j]:
        #             r+=s_rev[j]
        for i in range(length):
            counter = i
            rversIdx = 0
            while(counter<length):
                if s[counter] == s_rev[rversIdx]:{

                }
                      



        return r



if __name__ == '__main__':
    problem = "abacd"
    ss = Solution()
    result = ss.longestPalindrome(problem)
    print(result)