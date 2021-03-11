class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # r=[]
        # l = len(nums)
        # n1 = nums[0:n]
        # n2 = nums[n:]
        # for i in range(n):
        #     r.append(n1[i])
        #     r.append(n2[i])
        r=[]
        l = 2*n
        for i in range(n):
            r.append(nums[i])
            r.append(nums[n+i])
        return r

if __name__ == '__main__':
    s = Solution()
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    r = s.shuffle(nums,n)
    print(r)