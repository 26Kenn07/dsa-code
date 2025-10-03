class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = (n * (n+1)) // 2
        ls = 0

        for i in range(1, n+1):
            ls += i

            if ls == total - ls + i:
                return i

        return -1
