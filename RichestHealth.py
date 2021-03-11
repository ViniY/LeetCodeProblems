class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        mx = []
        for p in accounts:
            mx.append(sum(p))

        return max(mx)

if __name__ == '__main__':
    s = Solution()
    accounts = [[1, 2, 3], [3, 2, 1]]
    r = s.maximumWealth(accounts)
    print(r)