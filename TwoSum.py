class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j]==target:
                    r.append(i)
                    r.append(j)
                    return r


        return r

if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 4]
    target = 6
    r = s.twoSum(nums,target)
    print(r)