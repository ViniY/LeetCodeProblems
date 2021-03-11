class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        r = []
        mx_candies = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=mx_candies: ##can be equal
                r.append(True)
            else:
                r.append(False)
        return r

if __name__ == '__main__':
    s= Solution()
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    r = s.kidsWithCandies(candies,extraCandies)
    print(r)