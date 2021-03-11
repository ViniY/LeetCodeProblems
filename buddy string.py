class Solution(object):
    def buddyStrings(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        a_s = set(a)
        b_s = set(b)

        if len(a) != len(b) or a_s != b_s: return False  # If the length not equal then simply false
        if a == b:  # if a,b identical then check if there any character repeat
            return len(a) - len(b_s) >= 1
        else:
            counter = 0
            indices = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    counter += 1
                    if counter > 2: return False
                    indices.append(i)

            return a[indices[0]] == b[indices[1]] and a[indices[1]] == b[indices[0]]


if __name__ == '__main__':
    s = Solution()
    a = "ab"
    b = "ba"
    boolean = s.buddyStrings(a,b)
    print(boolean)