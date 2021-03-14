class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # counter = 0
        # mx = 0
        # start = 0
        # m = set()
        # for i in range(len(s)):
        #     if s[i] not in m:
        #         m.add(s[i])     # Add to a set
        #         counter += 1      # increase the counter by one
        #         print(i)
        #     else:
        #         m.clear()
        #         if mx < counter:
        #             mx = counter
        #         counter = 0
        #         start += 1
        #         i = int(start)
        #         i=i-1
        #         print(i)

        # i=0

        # while i< len(s):
        #     if s[i] not in m:
        #         m.add(s[i])     # Add to a set
        #         counter += 1      # increase the counter by one
        #         i += 1
        #     else:
        #         m.clear()
        #         if mx < counter:
        #             mx = counter
        #         counter = 0
        #         start += 1
        #         i = int(start)

        #
        # left = 0
        # right = 0
        # used = set()
        # mx = 0
        # if len(set(s)) == len(s): return len(s)
        # if len(set(s)) == 1: return 1
        # for i, c in enumerate(s):
        #     if c not in used:
        #         used.add(c)
        #         right += 1
        #     else:
        #         used.clear()
        #         mx = right - left
        #         left = i
        #         right = left
        #
        # if mx > (right - left):
        #     return mx
        # else:
        #     return right - left
        #40ms version
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length
        # if counter>mx: mx=counter
        # print(m)
        # return mx




if __name__ == '__main__':
    s = Solution()
    ss = "pwwkew"
    # ss = "aab"
    r = s.lengthOfLongestSubstring(ss)
    print(r)